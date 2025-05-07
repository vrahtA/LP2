def ask_yes_no_question(question):
   answer = input(question + " (yes/no): ").strip().lower()
   if answer in ["yes", "y"]:
      return True
   elif answer in ["no", "n"]:
      return False
   else:
      print("Invalid input. Please enter yes or no.")
def recommend_treatment_and_medicine(diagnosis):
   if diagnosis == "Flu":
      print("Recommended Medicine: Oseltamivir (Tamiflu), Paracetamol (for fever)")
      print("Recommended Tests: Rapid Influenza Diagnostic Test (RIDT), Blood Test")
      print(
         "Recommended Treatment: Rest, Hydration, Antiviral drugs (as prescribed by a doctor), Over-the-counter fever reducers")
   elif diagnosis == "Respiratory Infection":
      print("Recommended Medicine: Amoxicillin (Antibiotic), Paracetamol (for fever)")
      print("Recommended Tests: Chest X-ray, Sputum culture, Blood test")
      print("Recommended Treatment: Antibiotics (as prescribed), Cough syrup, Steam inhalation, Rest")
   elif diagnosis == "Malaria":
      print("Recommended Medicine: Artemisinin-based Combination Therapy (ACT), Chloroquine")
      print("Recommended Tests: Rapid Diagnostic Test (RDT), Blood Smear (for Plasmodium identification)")
      print("Recommended Treatment: Antimalarial drugs, Rest, Hydration, Antipyretics for fever")
   elif diagnosis == "Common Cold":
      print("Recommended Medicine: Paracetamol, Ibuprofen (for pain and fever), Decongestants")
      print("Recommended Tests: No tests required (symptomatic treatment)")
      print("Recommended Treatment: Rest, Hydration, Over-the-counter cold medicines")
   elif diagnosis == "Viral Infection":
      print("Recommended Medicine: Antipyretics (Paracetamol), Vitamin C supplements")
      print("Recommended Tests: Blood test, Viral culture (if needed)")
      print("Recommended Treatment: Rest, Hydration, Symptomatic treatment (fever reducers), Vitamin supplementation")
   elif diagnosis == "Stress or Fatigue":
      print("Recommended Medicine: Vitamin B12, Magnesium supplements, Antidepressants (if prescribed)")
      print("Recommended Tests: Blood test for anemia, Vitamin levels, Thyroid function test")
      print("Recommended Treatment: Stress management (meditation, yoga), Rest, Nutritional supplements")
   else:
      print("Recommended Medicine: Based on doctor's prescription")
      print("Recommended Tests: Based on symptoms")
      print("Recommended Treatment: Consult a doctor for a personalized treatment plan")

def diagnose():
   print("Welcome to the Hospital Expert System!")
   fever = ask_yes_no_question("Do you have a fever?")
   cough = ask_yes_no_question("Do you have a cough?")
   fatigue = ask_yes_no_question("Do you feel fatigued?")
   headache = ask_yes_no_question("Do you have a headache?")
   sore_throat = ask_yes_no_question("Do you have a sore throat?")
   shortness_of_breath = ask_yes_no_question("Do you have shortness of breath?")
   loss_of_taste_smell = ask_yes_no_question("Have you experienced a loss of taste or smell?")
   muscle_aches = ask_yes_no_question("Are you experiencing muscle aches?")
   nausea_vomiting = ask_yes_no_question("Do you have nausea or vomiting?")
   abdominal_pain = ask_yes_no_question("Are you experiencing abdominal pain?")

   if fever and cough and fatigue and headache:
      if loss_of_taste_smell:
         diagnosis = "Flu (possible COVID-19)"
      else:
         diagnosis = "Flu"
   elif fever and cough and sore_throat:
      diagnosis = "Respiratory Infection"
   elif fever and shortness_of_breath:
      diagnosis = "Viral Infection (COVID-19, Pneumonia)"
   elif fever and fatigue:
      diagnosis = "Malaria"
   elif cough and fatigue:
      diagnosis = "Common Cold"
   elif fatigue and headache:
      diagnosis = "Stress or Fatigue"
   elif fever:
      diagnosis = "Viral Infection"
   elif fatigue:
      diagnosis = "Fatigue-related condition"
   elif abdominal_pain and nausea_vomiting:
      diagnosis = "Gastrointestinal Issue"
   else:
      diagnosis = "No serious illness detected"


   print(f"\nDiagnosis: {diagnosis}")
   recommend_treatment_and_medicine(diagnosis)
   print("\nThank you for using the Hospital Expert System!")
   
if __name__ == "__main__":
   diagnose()
