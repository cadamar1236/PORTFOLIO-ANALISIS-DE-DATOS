import torch
from transformers import BertForQuestionAnswering, BertTokenizer
import gradio as gr

# Cargar el modelo y el tokenizador
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

def answer_question(text, question):
    print(question, text)
    inputs = tokenizer.encode_plus(question, text, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    with torch.no_grad():
        outputs = model(**inputs)
        answer_start_scores = outputs.start_logits
        answer_end_scores = outputs.end_logits
    
    answer_start = torch.argmax(answer_start_scores) 
    answer_end = torch.argmax(answer_end_scores) + 1 
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

    return answer

iface = gr.Interface(
    fn=answer_question, 
    inputs=["text", "text"], 
    outputs="text",
    title="BERT Question Answering",
    description="Modelo para responder preguntas usando BERT. Escribe un texto y una pregunta."
)

iface.launch(share=True)