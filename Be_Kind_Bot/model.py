import torch
from transformers import AutoTokenizer, AutoModel
import pickle

save_path = "ruben_small_bert"
model = AutoModel.from_pretrained(save_path, return_dict=True)
tokenizer = AutoTokenizer.from_pretrained(save_path)


def embed_bert_cls(text, m, t):
    t = t(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = m(**{k: v.to(m.device) for k, v in t.items()})
    embeddings = model_output.last_hidden_state[:, 0, :]
    embeddings = torch.nn.functional.normalize(embeddings)
    return embeddings[0].cpu().numpy()


filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


def check_rudeness(text):
    return bool(loaded_model.predict(embed_bert_cls(text, model, tokenizer).reshape(1, -1)))


print(check_rudeness('пошел нахуй блять'))
