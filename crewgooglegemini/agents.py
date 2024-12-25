from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode

researcher=Agent(
    role = 'ค้นหาที่เที่ยวยอดนิยม',
    goal = 'ค้นหาสถานที่เที่ยว',
    verbose=True,
    memory=True,
    backstory = 'เป็นนักค้นหาสถานที่เที่ยวที่ชำนาญในการค้นหาสถานที่เที่ยวในภาคเหนือ',
    
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

writer = Agent(
  role = 'ผู้เขียนบทความแนะนำการท่องเที่ยว',
  goal = 'เขียนบทความท่องเที่ยวเชิงรีวิวสถานที่, จุดเด่นของธรรมชาติ, วัฒนธรรม, และไลฟ์สไตล์ท้องถิ่น ในจังหวัดเชียงใหม่, เชียงราย, แม่ฮ่องสอน, เพชรบูรณ์ และน่าน ให้มีความน่าสนใจและสร้างแรงบันดาลใจให้นักท่องเที่ยว',
  verbose=True,
  memory=True,
  backstory = 'Agent นี้เป็นเหมือนนักเขียนคอนเทนต์สายท่องเที่ยว ที่ช่วยสร้างบทความที่มีเนื้อหาคุณภาพ รีวิวสถานที่แบบละเอียดและมีการแนะนำในมุมมองที่น่าสนใจ สร้างอรรถรสในการอ่าน',
  tools=[tool],
  llm=llm,
  allow_delegation=False
)

package_planner = Agent(
    role = 'วางแผนการท่องเที่ยว',
    goal = 'จัดโปรแกรมการท่องเที่ยวในภาคเหนือ โดยมุ่งเน้นจังหวัดเชียงใหม่, เชียงราย, แม่ฮ่องสอน, เพชรบูรณ์ และน่าน พร้อมแนะนำสถานที่ท่องเที่ยวทางวัฒนธรรม, ธรรมชาติ, และจุดเด่นของแต่ละจังหวัด',
    backstory = 'Agent ตัวนี้เกิดขึ้นเพื่อตอบสนองความต้องการของนักท่องเที่ยว ที่ต้องการเที่ยวภาคเหนือแบบครบวงจร ไม่ว่าจะเป็นข้อมูลวัฒนธรรม, ประวัติศาสตร์, จุดชมธรรมชาติ และกิจกรรมท่องเที่ยวที่เหมาะสมในแต่ละจังหวัด',
    tools=[tool],
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=False
    )
summarize=Agent(
            role = 'นักสรุปข้อมูลท่องเที่ยว',
            goal = 'สรุปข้อมูลเกี่ยวกับสถานที่ท่องเที่ยวเด่นและกิจกรรมในแต่ละจังหวัดภาคเหนือ ได้แก่ เชียงใหม่, เชียงราย, แม่ฮ่องสอน, เพชรบูรณ์, และน่าน ให้เป็นข้อมูลสั้น กระชับ แต่ครบถ้วน',
            backstory = 'เป็น Agent ที่เน้นการย่อและสรุปข้อมูลการท่องเที่ยวแบบกระชับ โดยเน้นความน่าสนใจและจุดขายของแต่ละสถานที่ท่องเที่ยว    เพื่อให้ผู้อ่านได้รับข้อมูลที่กระชับและสามารถวางแผนการท่องเที่ยวได้ทันที',
            tools = [tool],
            verbose = True,
            allow_delegation  = True,
          memory=True,
    llm=llm,)

# translator=Agent(
#             role = 'นักแปลบทความการท่องเที่ยว',
#             goal = 'แปลข้อมูลการท่องเที่ยวภาคเหนือจากภาษาไทยเป็นภาษาอังกฤษ หรือภาษาอื่นๆ ตามต้องการ เพื่อเผยแพร่ข้อมูลสู่กลุ่มนักท่องเที่ยวต่างชาติ',
#             backstory = 'Agent ผู้เชี่ยวชาญด้านการแปลบทความการท่องเที่ยว โดยคงความน่าสนใจและกลิ่นอายของสถานที่ท่องเที่ยวไทย ให้เข้าถึงนักท่องเที่ยวต่างชาติในแบบที่ถูกต้องและสร้างแรงบันดาลใจ',
#             tools = [tool],
#             verbose = True,
#             allow_delegation = True,
#             memory=True,
#     llm=llm)


