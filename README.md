# FAQ API with Multilingual Support

## **Objective**
The objective of this project is to evaluate the ability to design and implement a Django-based backend system for managing multilingual FAQs with WYSIWYG editor support, caching, and REST API integration.

---

## **Features**
- **Multilingual FAQs**: Store and retrieve FAQs in English, Hindi, and Bengali.
- **WYSIWYG Editor**: Rich text formatting using `django-ckeditor`.
- **Caching**: Redis integration for efficient API response caching.
- **Translation**: Automated translations via Google Translate API (`googletrans`).
- **REST API**: Language selection via query parameters (`?lang=`).
- **Admin Panel**: Django admin interface for FAQ management.
- **Unit Tests**: Comprehensive tests for models and API endpoints.

---

## **Task Requirements**

### **1. Model Design**
- **FAQ Model**:
  - Fields: `question_en` (TextField), `answer_en` (RichTextField).
  - Translations: `question_hi`, `answer_hi`, `question_bn`, `answer_bn`.
  - Methods: `get_translated_question(lang)`, `get_translated_answer(lang)`.

### **2. WYSIWYG Editor**
- Integrated `django-ckeditor` for answer formatting in the admin panel.

### **3. API Development**
- **Endpoints**:
  - `GET /api/faqs/?lang=<lang>`: Fetch FAQs in the specified language.
- **Efficiency**: Pre-translation and Redis caching for fast responses.

### **4. Caching**
- **Redis**: Cache translations for 15 minutes.
- **Invalidation**: Clear cache on FAQ updates/deletes.

### **5. Translation**
- **Automation**: Translate FAQs during creation using `googletrans`.
- **Fallback**: Default to English if translation fails.

### **6. Admin Panel**
- Registered `FAQ` model with CKEditor widgets for multilingual fields.

### **7. Testing**
- **Tools**: `pytest` for unit tests.
- **Coverage**: Models, API responses, and caching logic.

### **8. Documentation**
- **README**: Installation steps, API examples, contribution guidelines.

### **9. Git Practices**
- **Commits**: Follow conventional commit messages (e.g., `feat: Add model`).
- **Branching**: Atomic commits with clear descriptions.

### **10. Deployment (Bonus)**
- **Docker**: `Dockerfile` and `docker-compose.yml` included.
- **Hosting**: Optional deployment to Heroku/AWS.

---

## **Installation**

### **Prerequisites**
- Python 3.9+
- Redis
- Docker (optional)

# FAQ API Setup
# FAQ API Project

## API Usage:
- **Fetch FAQs:**
  - Hindi: `curl http://localhost:8000/api/faqs/?lang=hi`
  - Bengali: `curl http://localhost:8000/api/faqs/?lang=bn`
  - English (default): `curl http://localhost:8000/api/faqs/`

## Admin Panel:
- **Access:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **Create a Superuser:** `python manage.py createsuperuser`
- **Manage FAQs:** Use the WYSIWYG editor for FAQ content management.

## Caching:
- **Cache Duration:** 15 minutes.
- **Cache Invalidation:** Automatically cleared upon FAQ updates or deletions.

## Translation Workflow:
- **Automated:** Translations are handled automatically when FAQs are created.
- **Fallback:** If a translation fails, English text is used by default.

## Testing:
- **Run Tests:** Execute `pytest` to run the tests for your project.

## Docker Deployment:
- **Build and Run:** `docker-compose up --build`
- **API Access:** The API can be accessed at [http://localhost:8000/api/faqs/](http://localhost:8000/api/faqs/).

## Evaluation Criteria:
- **Code Quality:** Ensure adherence to PEP8 and modular code structure.
- **Functionality:** Focus on correct API responses, multilingual functionality, and caching.
- **Documentation:** Clear README with setup instructions and project details.
- **Testing:** Ensure models and APIs are properly tested.
- **Git Practices:** Maintain clean commit messages and project structure.


## License:
- **MIT License:** Ensure the repository includes the proper licensing details.

## Contact:
- **GitHub:** happy2234
- **Email:** gauravjangra@1110.com

## Skills Demonstrated:
- Django models, REST APIs, caching, internationalization (i18n), documentation, testing, and Docker deployment.


   
