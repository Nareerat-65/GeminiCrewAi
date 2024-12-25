from crewai import Crew, Process
from tasks import research_task, write_task, package_planner_task, summarize_travel_task
from agents import researcher, writer, package_planner, summarize

# Forming the tech focused crew with some enhanced configuration
crew = Crew(
    agents=[researcher, writer, package_planner, summarize],
    tasks=[research_task, write_task, package_planner_task, summarize_travel_task],
    process=Process.sequential,
)

# Prompting the user for multiple inputs
day_input = input("ไปกี่วัน : ")
people_input = input("ไปกี่คน : ")
location_input = input("จังหวัดที่ต้องการไป (น่าน, เชียงใหม่, เชียงราย, แม่ฮ่องสอน, เพชรบูรณ์) : ")
interest_input = input("ความสนใจ (ธรรมชาติ, วัด, etc.) : ")

# Update the expected_output for tasks
research_task.expected_output = research_task.expected_output.format(day_input=day_input, people_input=people_input, location_input=location_input, interest_input=interest_input)
package_planner_task.expected_output = package_planner_task.expected_output.format(day_input=day_input, location_input=location_input)
summarize_travel_task.expected_output = summarize_travel_task.expected_output.format(day_input=day_input, people_input=people_input, location_input=location_input, interest_input=interest_input)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={"Day": day_input, "People": people_input, "Location": location_input, "Interest": interest_input})
print(result)