from flask import Blueprint, request, jsonify, render_template, current_app
from .services.translate import translate_text
from .services.nlp import analyze_text
from .models import db, Translation

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/health')
def health():
    return jsonify({'status':'ok'})

@bp.route('/api/translate/text', methods=['POST'])
def translate_text_endpoint():
    data = request.get_json() or {}
    text = data.get('text')
    if not text:
        return jsonify({'error':'missing text'}), 400

    # 1) normalize / analyze
    tokens = analyze_text(text)

    # 2) translate
    result = translate_text(text)

    # 3) save to DB (optional)
    try:
        t = Translation(input_text=text, input_type='text', result_mm=result.get('mm'))
        db.session.add(t)
        db.session.commit()
    except Exception:
        db.session.rollback()

    return jsonify({'jp': text, 'mm': result.get('mm'), 'tokens': tokens})
