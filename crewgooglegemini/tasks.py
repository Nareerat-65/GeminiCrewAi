from crewai import Task
from tools import tool
from agents import researcher,writer,package_planner,summarize

# Research task
research_task = Task(
  description = "ช่วยแนะนำสถานที่ท่องเที่ยวยอดนิยมในจังหวัดภาคเหนือ โดยระบุข้อมูลสำคัญ เช่น ชื่อสถานที่, ประเภท, จุดเด่น และพิกัด เพื่อให้ผู้ใช้สามารถวางแผนการเดินทางได้อย่างมีประสิทธิภาพ",
  expected_output='ค้นหาสถานที่ท่องเที่ยวในภาคเหนือในจังหวัด เชียงใหม่, เชียงราย, แม่ฮ่องสอน,เพชรบูรณ์และน่านจำเป็นต้องค้นหาสถานที่ท่องเที่ยวที่เป็นข้อมูลที่ถูกต้องและมีความสำคัญพร้อมรายละเอียดที่เป็นประโยชน์แก่นักเที่ยว',
  tools=[tool],
  agent=researcher,
)

# Writing task with language model configuration
write_task = Task(
  description="นักเขียนที่ชำนาญในการเขียนสถานที่ท่องเที่ยวยอดนิยมในจังหวัด เชียงใหม่, เชียงราย, แม่ฮ่องสอน, เพชรบูรณ์และน่าน มีความสามารถในการเขียนสถานที่ท่องเที่ยวยอดนิยมในจังหวัดเหล่านี้ให้สรุปและเข้าใจง่าย",
  expected_output="เขียนสถานที่ท่องเที่ยวตามข้อมูลที่ได้รับมา โดยนำข้อมูลสถานที่ท่องเที่ยวที่ได้รับมา มาเขียนสรุป เข้าใจง่าย และเป็นภาษาไทย",
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file='writer.md'  # Example of output customization
)
package_planner_task = Task(
  description="ช่วยวิเคราะห์สถานที่ท่องเที่ยวยอดนิยมจังหวัดเชียงใหม่, เชียงราย, แม่ฮ่องสอน, เพชรบูรณ์, น่าน ที่ได้รับมาวิเคราะห์ เพื่อนำข้อมูลสถานที่ท่องเที่ยวมาสรุปให้นักท่องเที่ยว",
  expected_output="วางแผนท่องเที่ยวตามจำนวนวัน {day_input} โดยนำข้อมูลสถานที่ท่องเที่ยวที่ได้รับมา มาวางแผนการท่องเที่ยวให้เหมาะสม และเข้าใจง่าย เป็นภาษาไทย",
  tools=[tool],
  agent=package_planner,
  async_execution=False,
  output_file='planner.md'  # Example of output customization
)
summarize_travel_task = Task(
  description="สรุปสถานที่ท่องเที่ยวที่ได้รับ โดยนำสถานที่ท่องเที่ยวที่ได้รับมาสรุปให้สั้นกระชับและเข้าใจง่าย",
  expected_output="สรุปสถานที่ท่องเที่ยวที่ได้ทำการวิเคราะห์มาแล้วให้กระชับเข้าใจง่ายและเป็นภาษาไทย",
  tools=[tool],
  agent=summarize,
  async_execution=False,
  output_file='summarize.md'  # Example of output customization
)

# translator_task = Task(
#   description="แปลบทความสถานที่ท่องเที่ยวยอดนิยมที่ได้รับจากภาษาอังกฤษเป็นภาษาเป้าหมาย",
#   expected_output = "แปลบทความสถานที่ท่องเที่ยวยอดนิยมที่ได้รับจากภาษาอังกฤษเป็นภาษาเป้าหมาย โดยทำให้เนื้อหาสามารถเข้าใจได้ง่ายและถูกต้องทางภาษา รวมถึงรักษาความหมายเดิมของสถานที่ท่องเที่ยวโดยไม่บิดเบือน",
  
#   tools=[tool],
#   agent=translator,
#   async_execution=False,
#   output_file='planner.md'  # Example of output customization
# )
