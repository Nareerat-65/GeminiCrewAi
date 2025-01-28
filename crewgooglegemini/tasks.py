from crewai import Task
from tools import tool
from agents import researcher, writer, package_planner, summarize

# Research task
research_task = Task(
    description="ค้นหาสถานที่ท่องเที่ยวยอดนิยมในจังหวัดภาคเหนือ พร้อมที่พักและร้านอาหารแนะนำ โดยระบุชื่อสถานที่, ประเภท, จุดเด่น, เวลาเปิด-ปิด และพิกัด Google Maps เพื่อช่วยวางแผนการเดินทาง",
    expected_output="ค้นหาสถานที่ท่องเที่ยว ที่พัก ร้านอาหาร จาก {location_input} สำหรับ {day_input} วัน จำนวน {people_input} คน พร้อมรายละเอียดที่สอดคล้องกับความสนใจ {interest_input}",
    tools=[tool],
    agent=researcher,
    max_token=500
)

# Writing task with language model configuration
write_task = Task(
    description="นักเขียนที่เชี่ยวชาญในการสรุปข้อมูลสถานที่ท่องเที่ยวยอดนิยมในจังหวัดที่กำหนด โดยสรุปเนื้อหาให้อ่านง่ายและเข้าใจได้ในภาษาไทย",
    expected_output="สรุปข้อมูลสถานที่ท่องเที่ยวตามที่ได้รับให้อ่านง่าย ชัดเจน และเป็นภาษาไทย",
    tools=[tool],
    agent=writer,
    async_execution=False,
    max_token=500
)

# Package planner task
package_planner_task = Task(
    description="วิเคราะห์และสรุปสถานที่ท่องเที่ยวยอดนิยมในจังหวัดที่กำหนด เพื่อวางแผนการเดินทางที่เหมาะสมสำหรับนักท่องเที่ยว",
    expected_output="วางแผนการท่องเที่ยว {day_input} วันในจังหวัด {location_input} โดยระบุชื่อสถานที่, ที่พักและร้านอาหารในแต่ละวัน พร้อมเวลาเปิด-ปิด, ราคาที่พักต่อคืน และพิกัด Google Maps สรุปเนื้อหาให้อ่านง่ายและเป็นภาษาไทย",
    tools=[tool],
    agent=package_planner,
    async_execution=False,
    output_file="planner.md",
    max_token=500
)


# Summarize travel task
summarize_travel_task = Task(
    description="สรุปข้อมูลสถานที่ท่องเที่ยวที่กำหนดให้อย่างกระชับและเข้าใจง่าย",
    expected_output="สรุปแผนการท่องเที่ยวในจังหวัด {location_input} สำหรับ {day_input} วัน จำนวน {people_input} คน พร้อมรายละเอียดที่ตรงกับความสนใจ {interest_input} โดยเน้นข้อมูลที่เป็นประโยชน์และเข้าใจง่าย",
    tools=[tool],
    agent=summarize,
    async_execution=False,
    max_token=500
)