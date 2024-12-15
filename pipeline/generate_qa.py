from transformers import AutoTokenizer, AutoModelForSeq2SeqLM 

# Initialize the model and tokenizer

# original model path 
model_path = "potsawee/t5-large-generation-squad-QuestionAnswer"

# fine tuned model path - lora - no such directory exists!! 
# model_path = "/content/finetuned_squad"

# fine tuned model path - lora + pos 
# model_path = "Squad/t5squad_ner-pos_finetuned_sciq_7"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path) 

model = PeftModel.from_pretrained(model, model_path)

def gen_qa(context, num_questions=5):
    """
    Generate multiple question-answer pairs from the given context.
    """
    questions_answers = []
    context_length = len(context)
    overlap = 20  # Number of overlapping words
    chunk_size = (context_length - overlap * (num_questions - 1)) // num_questions

    questions_answers = []
    for i in range(num_questions):
        start_idx = i * chunk_size - i * overlap
        end_idx = start_idx + chunk_size
        if end_idx > context_length:
            end_idx = context_length

        chunk = context[start_idx:end_idx]

        # chunk size needs to be <512, return a summary of the chunk within length 512
        # if len(chunk) > 512:
            # chunk = summary of chunk
        
        # Generate question-answer pair as before
        inputs = tokenizer(chunk, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=100, num_return_sequences=1, num_beams=4)
        question_answer = tokenizer.decode(outputs[0], skip_special_tokens=False)
        question_answer = question_answer.replace(tokenizer.pad_token, "").replace(tokenizer.eos_token, "")
        
        if tokenizer.sep_token in question_answer:
            question, answer = question_answer.split(tokenizer.sep_token)
            questions_answers.append((question, answer))

    return questions_answers




