import streamlit as st
import spacy

nlp = spacy.load("en_core_web_lg")

def extract_entities(ent_types, text):
    doc