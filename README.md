# 7-5-Universal-Study-Quiz-An-Active-Learning-Tool

📝 This Python-based program is a versatile Self-Study Tool designed for students who want to master any subject through active recall. While it currently features questions on the properties of water, the modular design allows users to easily swap out the dataset for any academic topic—from Chemistry to History or Computer Science.


🚀 Key Learning Features

- Customizable Curriculum: Users can add any question-answer pairs to quiz_data.py, making it a perfect companion for exam preparation in any course. 

- Timed Recall (Spaced Repetition): The 60-second limit forces students to retrieve information quickly, strengthening memory retention and preparing them for timed exams. 

- Logical Distractors: The program automatically generates decoy answers. For math or science, it generates nearby numerical values to test precision; for text, it draws from other entries to ensure students truly understand the correct pairing. 

- Gamified Feedback Loop:

  - 3 Attempts per Question - Encourages students to rethink their logic before seeing the final answer.
  - Penalty System: Penalizes wrong guesses or timeouts to discourage guessing and promote mastery. 
	
- Optimized Study Interface: The clear_screen function keeps the student's focus solely on the current question, minimizing cognitive overload.


📂 How to Add Your Own Questions

 
  1. Open quiz_data.py.
	
  2. Insert your questions as Keys and answers as Values inside the Python dictionary. 
	
  3. For numerical answers (e.g., $4^\circ C$), use integers to trigger the automatic number generator for distractors. 
	
  4. For text answers (e.g., "Aqueous solution"), use strings to pull distractors from your other answers.

  
🛠 Installation & Usage

   - To use the timeout feature for your study sessions, install the required library by copying the following code to VSCode's Terminal: pip install func_timeout


Developer Note: Designed as a tool for students at Ensign College to build "muscle memory" in programming and academic recall.
