from flask import Flask, render_template, request
from crewai import Crew, Process
from tasks import research_task, write_task, package_planner_task, summarize_travel_task
from agents import researcher, writer, package_planner, summarize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def plan():
    day_input = request.form['day']
    people_input = request.form['people']
    location_input = request.form['location']
    interest_input = request.form['interest']

    # Update the expected_output for tasks
    research_task.expected_output = research_task.expected_output.format(day_input=day_input, people_input=people_input, location_input=location_input, interest_input=interest_input)
    package_planner_task.expected_output = package_planner_task.expected_output.format(day_input=day_input, location_input=location_input)
    summarize_travel_task.expected_output = summarize_travel_task.expected_output.format(day_input=day_input, people_input=people_input, location_input=location_input, interest_input=interest_input)

    # Forming the tech focused crew with some enhanced configuration
    crew = Crew(
        agents=[researcher, writer, package_planner, summarize],
        tasks=[research_task, write_task, package_planner_task, summarize_travel_task],
        process=Process.sequential,
    )

    # Starting the task execution process with enhanced feedback
    result = crew.kickoff(inputs={"Day": day_input, "People": people_input, "Location": location_input, "Interest": interest_input})

    # Write the result to planner.md
    with open('planner.md', 'w', encoding='utf-8') as f:
        f.write(result)

    return render_template('planner.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)