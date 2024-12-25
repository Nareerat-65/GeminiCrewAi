from crewai import Task
from tools import tool
from agents import researcher, writer, package_planner, summarize

# Research task
research_task = Task(
  description="ช่วยแนะนำสถานที่ท่องเที่ยวยอดนิยมในจังหวัดภาคเหนือ โดยระบุข้อมูลสำคัญ เช่น ชื่อสถานที่, ประเภท, จุดเด่น และพิกัด เพื่อให้ผู้ใช้สามารถวางแผนการเดินทางได้อย่างมีประสิทธิภาพ",
  expected_output='ค้นหาสถานที่ท่องเที่ยว ที่พัก ร้านอาหาร โดยอ้างอิงจาก {location_input} สำหรับ {day_input} วัน จำนวน {people_input} คน ความสนใจ {interest_input} จำเป็นต้องค้นหาสถานที่ท่องเที่ยวที่เป็นข้อมูลที่ถูกต้องและมีความสำคัญพร้อมรายละเอียดที่เป็นประโยชน์แก่นักเที่ยว',
  tools=[tool],
  agent=researcher,
)

# Writing task with language model configuration
write_task = Task(
  description="นักเขียนที่ชำนาญในการเขียนสถานที่ท่องเที่ยวยอดนิยมในจังหวัดที่ได้รับมา และมีความสามารถในการเขียนสถานที่ท่องเที่ยวยอดนิยมในจังหวัดนี้ให้สรุปและเข้าใจง่าย",
  expected_output="เขียนสถานที่ท่องเที่ยวตามข้อมูลที่ได้รับมา โดยนำข้อมูลสถานที่ท่องเที่ยวที่ได้รับมา มาเขียนสรุป เข้าใจง่าย และเป็นภาษาไทย",
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file='writer.md'  # Example of output customization
)

# Package planner task
package_planner_task = Task(
  description="ช่วยวิเคราะห์สถานที่ท่องเที่ยวยอดนิยมในจังหวัดที่ได้รับ มาวิเคราะห์ เพื่อนำข้อมูลสถานที่ท่องเที่ยวมาสรุปให้นักท่องเที่ยว",
  expected_output="วางแผนการท่องเที่ยวตามจำนวนวัน {day_input}กำนดเวลาในแต่ละวัน ในจังหวัด{location_input} โดยนำข้อมูลสถานที่ท่องเที่ยวที่ได้รับมา มาวางแผนการท่องเที่ยวให้เหมาะสม และเข้าใจง่าย เป็นภาษาไทย",
  tools=[tool],
  agent=package_planner,
  async_execution=False,
  output_file='planner.md'  # Example of output customization
)

# Summarize travel task
summarize_travel_task = Task(
  description="สรุปสถานที่ท่องเที่ยวที่ได้รับ โดยนำสถานที่ท่องเที่ยวที่ได้รับมาสรุปให้สั้นกระชับและเข้าใจง่าย",
  expected_output="สรุปการเดินทางท่องเที่ยวในจังหวัด {location_input} สำหรับ {day_input} วัน จำนวน {people_input} คน ความสนใจ {interest_input} โดยสรุปข้อมูลที่เป็นประโยชน์และเข้าใจง่าย",
  tools=[tool],
  agent=summarize,
  async_execution=False,
  output_file='summarize.md'  # Example of output customization
)