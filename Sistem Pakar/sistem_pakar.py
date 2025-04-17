# -*- coding: utf-8 -*-
"""Sistem pakar

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hvXTsmvFZCoUpxJ9eJWO8IeKyYRq9sOh
"""

!pip install experta

!pip install --upgrade frozendict

from experta import *

class Diagnosis(KnowledgeEngine):

  @Rule(Fact(cough=True) & Fact(fever=True) & Fact(fatigue=True))
  def flu(self):
    print("Diagnosis: you may have the flu")

  @Rule(Fact(cough=True) & Fact(fever=True) & Fact(breathing_difficulty=True))
  def pneumonia(self):
    print("Diagnosis : you may have pneumonia")

  @Rule(Fact(sneezing=True) & Fact(runny_nose=True) & Fact(cough=False))
  def cold(self):
    print("Diagnosis : you may have a common cold.")

  @Rule(Fact(sore_throat=True) & Fact(fever=True))
  def throat_infection(self):
    print("Diagnosis : you may have a throat infection")

  # Penyakit tambahan:
  @Rule(Fact(fever=True) & Fact(headache=True) & Fact(muscle_pain=True))
  def dengue(self):
    print("Diagnosis : you may have dengue fever")

  @Rule(Fact(nausea=True) & Fact(vomiting=True) & Fact(diarrhea=True))
  def food_poisoning(self):
    print("Diagnosis : you may have food poisoning")

  @Rule(Fact(cough=True) & Fact(wheezing=True) & Fact(breathing_difficulty=True))
  def asthma(self):
    print("Diagnosis : you may have asthma")

  @Rule(Fact(sneezing=True) & Fact(runny_nose=True) & Fact(itchy_eyes=True))
  def allergy(self):
    print("Diagnosis : you may have an allergy")

  @Rule(Fact(cough=False) & Fact(fever=False) & Fact(fatigue=False))
  def healthy(self):
    print("Diagnosis : you seem to be healthy")


def get_input():
  """Helper function to get user input as boolean(yes/no)."""
  def ask_question(question):
    return input(question + " (yes/no): ").strip().lower() == "yes"

  return{
      "cough": ask_question("Do you have a cough?"),
      "fever": ask_question("Do you have a fever?"),
      "fatigue": ask_question("Do you feel fatigued?"),
      "breathing_difficulty": ask_question("Do you have breathing difficulties?"),
      "sneezing": ask_question("Are you sneezing?"),
      "runny_nose": ask_question("Do you have a runny nose?"),
      "sore_throat": ask_question("Do you have a sore throat?"),
      "headache": ask_question("Do you have a headache?"),
      "muscle_pain": ask_question("Are you experiencing muscle pain?"),
      "nausea": ask_question("Do you feel nauseous?"),
      "vomiting": ask_question("Are you vomiting?"),
      "diarrhea": ask_question("Do you have diarrhea?"),
      "wheezing": ask_question("Are you wheezing?"),
      "itchy_eyes": ask_question("Do you have itchy eyes?")
  }

if __name__== "__main__":
  symptoms = get_input()
  engine = Diagnosis()
  engine.reset()

  for symptom, present in symptoms.items():
    engine.declare(Fact(**{symptom: present}))

  engine.run()

from experta import *

class SistemPakarMedis(KnowledgeEngine):

  @Rule(Fact(demam=True) & Fact(batuk=True))
  def flu(self):
    print("diagnosist anda flu")

  @Rule(Fact(sakit_tenggorokan=True) & Fact(demam=False))
  def throat_infection(self):
    print("diagnosist radang ternggorokan")

  @Rule(Fact(nyeri_otot=True) & Fact(nyeri_perut=True))
  def hernia(self):
    print("diagnosis hernia")

engine = SistemPakarMedis()
engine.reset()

engine.declare(Fact(demam=True))
engine.declare(Fact(batuk=True))
engine.run()

def forward_chaining(facts, rules):
  inferred_facts = set(facts)
  changed = True
  while changed:
    changed = False
    for rule in rules:
      if rule["if"].issubset(inferred_facts) and rule["then"] not in inferred_facts:
        inferred_facts.add(rule["then"])
        changed = True
  return inferred_facts

facts = {"has_feather", "has_beak", "carnivore"}
rules = [
    {"if": {"has_feather", "has_beak"}, "then": "is_bird"},
    {"if": {"lays_egg", "is_bird"}, "then": "is_chicken"},
    {"if": {"cannot_fly", "is_bird"}, "then": "is_penguin"},
    {"if": {"carnivore", "is_bird"}, "then": "is_eagle"}
]

result = forward_chaining(facts, rules)
print("Inferred facts:", result)

def backward_chaining(goal, facts, rules):
    if goal in facts:
      return True
    for rule in rules:
      if rule["then"] == goal:
        if all(backward_chaining(cond, facts, rules) for cond in rule["if"]):
          return True
    return False

facts = {"likes_computers", "solves_problems", "likes_to_design"}
rules = [
    {"if": {"likes_computers", "solves_problems"}, "then": "should_be_engineer"},
    {"if": {"should_be_engineer", "likes_programming"}, "then": "software_engineer"},
    {"if": {"should_be_engineer", "likes_to_design"}, "then": "UI/UX_engineer"},
]

goal = "UI/UX_engineer"
result = backward_chaining(goal, facts, rules)
print(f"Is '{goal}' provable? ->", result)

def forward_chaining(facts, rules):
  inferred_facts = set(facts)
  changed = True

  while changed:
    changed = False
    for rule in rules:
      if rule["if"].issubset(inferred_facts) and rule["then"] not in inferred_facts:
        inferred_facts.add(rule["then"])
        changed = True
  return inferred_facts

facts = {"has_wheels", "has_engine", "has_four_wheels"}
rules= [
    {"if": {"has_wheels", "has_engine"}, "then": "is_vehicle"},
    {"if": {"is_vehicle", "has_two_wheels"}, "then": "is_motorcycle"},
    {"if": {"is_vehicle", "has_four_wheels"}, "then": "is_car"}
]

result = forward_chaining(facts, rules)
print("Inferred facts:", result)

def backward_chaining(goal, facts, rules):
  if goal in facts:
    return True
  for rule in rules:
    if rule["then"] == goal:
      if all(backward_chaining(cond, facts, rules) for cond in rule["if"]):
        return True
  return False

facts = {"has_feather", "has_small_wings"}
rules = [
    {"if": {"is_bird", "cannot_fly"}, "then": "is_penguin"},
    {"if": {"has_feather"}, "then": "is_bird"},
    {"if": {"has_small_wings"}, "then": "cannot_fly"},
]

goal = "is_penguin"
result = backward_chaining(goal, facts, rules)
print(f"Is '{goal}' provable? ->", result)