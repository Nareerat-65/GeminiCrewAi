from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Call the gemini models
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"),
                             language="th",
                             max_token=1000)

# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
    role='ค้นหาที่เที่ยวยอดนิยม',
    goal='ค้นหาสถานที่เที่ยว',
    verbose=False,
    memory=True,
    backstory='เป็นนักค้นหาสถานที่เที่ยวที่ชำนาญในการค้นหาสถานที่เที่ยวในภาคเหนือ',
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a write agent with custom tools responsible in writing news blog
writer = Agent(
    role='ผู้เขียนบทความแนะนำการท่องเที่ยว',
    goal='เขียนบทความท่องเที่ยวเชิงรีวิวสถานที่, จุดเด่นของธรรมชาติ, วัฒนธรรม, และไลฟ์สไตล์ท้องถิ่น ในจังหวัดที่ได้รับ ให้มีความน่าสนใจและสร้างแรงบันดาลใจให้นักท่องเที่ยว',
    verbose=False,
    memory=True,
    backstory='Agent นี้เป็นเหมือนนักเขียนคอนเทนต์สายท่องเที่ยว ที่ช่วยสร้างบทความที่มีเนื้อหาคุณภาพ รีวิวสถานที่แบบละเอียดและมีการแนะนำในมุมมองที่น่าสนใจ สร้างอรรถรสในการอ่าน',
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

# Creating a package planner agent
package_planner = Agent(
    role='วางแผนการท่องเที่ยว',
    goal='จัดโปรแกรมการท่องเที่ยวในภาคเหนือ โดยมุ่งเน้นจังหวัดที่ได้รับ พร้อมแนะนำสถานที่ท่องเที่ยวทางวัฒนธรรม, ธรรมชาติ, และจุดเด่นของแต่ละจังหวัด',
    verbose=False,
    memory=True,
    backstory='Agent ตัวนี้เกิดขึ้นเพื่อตอบสนองความต้องการของนักท่องเที่ยว ที่ต้องการเที่ยวภาคเหนือแบบครบวงจร ไม่ว่าจะเป็นข้อมูลวัฒนธรรม, ประวัติศาสตร์, จุดชมธรรมชาติ และกิจกรรมท่องเที่ยวที่เหมาะสมในแต่ละจังหวัด',
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

# Creating a summarize agent
summarize = Agent(
    role='นักสรุปข้อมูลท่องเที่ยว',
    goal='สรุปข้อมูลการเดินทางท่องเที่ยวในภาคเหนือ โดยระบุข้อมูลสำคัญ เช่น ชื่อสถานที่, ประเภท, จุดเด่น และพิกัด เพื่อให้ผู้ใช้สามารถวางแผนการเดินทางได้อย่างมีประสิทธิภาพ',
    verbose=False,
    memory=True,
    backstory='เป็น Agent ที่เน้นการย่อและสรุปข้อมูลการท่องเที่ยวแบบกระชับ โดยเน้นความน่าสนใจและจุดขายของแต่ละสถานที่ท่องเที่ยว เพื่อให้ผู้อ่านได้รับข้อมูลที่กระชับและสามารถวางแผนการท่องเที่ยวได้ทันที',
    tools=[tool],
    llm=llm,
    allow_delegation=True
)