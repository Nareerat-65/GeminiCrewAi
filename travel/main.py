from agent_task import AgentTasks
from travel_agent import TravelAgent
from crewai import Crew 
from dotenv import load_dotenv

load_dotenv()

class TravelCrew: 
    def run(self):
        agents = TravelAgent()
        tasks = AgentTasks()
        
        agents_search_travel = agents.searcher()
        agents_package_travel = agents.package_planner()
        agents_summarize_travel = agents.summarize()
        agents_writer_travel = agents.writer()
        agents_translator_travel = agents.translator()

        tasks_search_travel = tasks.search_travel(agents_search_travel)
        tasks_package_travel = tasks.analyze_travel(agents_package_travel)
        tasks_summarize_travel = tasks.summarize_travel(agents_summarize_travel)
        tasks_writer_travel = tasks.writer_travel(agents_writer_travel)
        tasks_translator_travel = tasks.translator_travel(agents_translator_travel)

        crew = Crew(
            agents = [agents_search_travel, agents_package_travel, agents_summarize_travel, agents_writer_travel, agents_translator_travel],
            tasks = [tasks_search_travel, tasks_package_travel, tasks_summarize_travel, tasks_writer_travel, tasks_translator_travel],
            verbose = True
        )

        result = crew.run()
        return result

if __name__ == '__main__':
    travel_crew = TravelCrew()
    travel_crew.run()
