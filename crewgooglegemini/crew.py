from crewai import Crew,Process
from tasks import research_task,write_task, package_planner_task, summarize_travel_task
from agents import researcher,writer,package_planner,summarize

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[researcher,writer,package_planner,summarize],
    tasks=[research_task,write_task, package_planner_task, summarize_travel_task],
    process=Process.sequential,

)

## Input from the user
day_input = input("Please enter the day: ")
people_input = input("Please enter the number of people: ")
loaction_input = input("จังหวัดที่ต้องการไป (น่าน, เชียงใหม่, เชียงราย, แม่ฮ่องสอน, เพชรบูรณ์): ")
interest_input = input("Please enter the interest (ธรรมชาติ, วัด, etc.): ")

## formatting the expected output
package_planner_task.expected_output = package_planner_task.expected_output.format(day_input=day_input)

## Running the crew
result=crew.kickoff(inputs={"Day" : day_input, "Location" : loaction_input, "People" : people_input, "Interest" : interest_input})
print(result)