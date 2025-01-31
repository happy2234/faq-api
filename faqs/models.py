from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question_en = models.TextField()
    answer_en = RichTextField()
    question_hi = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)
    question_bn = models.TextField(blank=True)
    answer_bn = RichTextField(blank=True)

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question_en)

    def get_translated_answer(self, lang):
        return getattr(self, f'answer_{lang}', self.answer_en)

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            from googletrans import Translator
            translator = Translator()
            for lang in ['hi', 'bn']:
                try:
                    setattr(self, f'question_{lang}', translator.translate(self.question_en, dest=lang).text)
                    setattr(self, f'answer_{lang}', translator.translate(self.answer_en, dest=lang).text)
                except Exception as e:
                    pass
            super().save(*args, **kwargs)