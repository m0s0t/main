import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# قاعدة بيانات للأدوية (تأكد من وجود الصور في مجلد images)
drugs = {
    "Propofol": {
        "dose_range_mg_per_kg": [1.5, 2.5],
        "side_effects": "Sedation; Depresses respiration; Decreases BP",
        "administration_routes": ["IV"],
        "notes": "مناسب للتهدئة السريعة والتحكم في مستوى الوعي.",
        "contraindications": "حساسية تجاه البروبوبوفول؛ اضطرابات في ضغط الدم.",
        "image_path": "images/Propofol.png"
    },
    "Ketamine": {
        "dose_range_mg_per_kg": [1, 2],
        "side_effects": "Stimulates nervous system; Maintains respiration; Increases BP",
        "administration_routes": ["IV", "IM"],
        "notes": "مفيد في التخدير مع الحفاظ على التنفس؛ مناسب للمرضى الذين يحتاجون لدعم القلب.",
        "contraindications": "مرضى ارتفاع ضغط الدم؛ مرضى الصرع.",
        "image_path": "images/ketamine.png"
    },
    "Etomidate": {
        "dose_range_mg_per_kg": [0.2, 0.6],
        "side_effects": "Sedation; Depresses respiration; Stable BP",
        "administration_routes": ["IV"],
        "notes": "مفيد للمرضى الذين يعانون من اضطرابات قلبية لأنه يحافظ على ضغط الدم.",
        "contraindications": "الصدفية النشطة؛ حساسية تجاه المادة.",
        "image_path": "images/Etomidate.png"
    },
    "Thiopental": {
        "dose_range_mg_per_kg": [3, 5],
        "side_effects": "Sedation; Depresses respiration; Decreases BP",
        "administration_routes": ["IV"],
        "notes": "يستخدم للتخدير العام السريع، لكن يحتاج مراقبة دقيقة للوظائف الحيوية.",
        "contraindications": "الربو؛ أمراض القلب الحادة.",
        "image_path": "images/Thiopental.png"
    },
    "Midazolam": {
        "dose_range_mg_per_kg": [0.05, 0.1],
        "side_effects": "Sedation; Amnesia; Minimal respiratory and cardiovascular effects",
        "administration_routes": ["IV", "IM"],
        "notes": "مناسب لتهدئة المرضى قبل الإجراءات القصيرة، ويتميز بخاصية فقدان الذاكرة المؤقت.",
        "contraindications": "الحساسية للبنزوديازيبينات؛ الأمراض التنفسية الشديدة.",
        "image_path": "images/Midazolam.png"
    },
    "Dexmedetomidine": {
        "dose_range_mcg_per_kg_per_hr": [0.2, 1.0],
        "side_effects": "Sedation; Maintains respiration; Stable BP",
        "administration_routes": ["IV"],
        "notes": "مناسب للتهدئة في العناية المركزة مع أقل تأثير على التنفس.",
        "contraindications": "الصدمة؛ انخفاض ضغط الدم الحاد.",
        "image_path": "images/Dexmedetomidine.png"
    },
    "Lidocaine": {
        "dose_range_mg_per_kg": [0.5, 1],
        "side_effects": "Analgesic effects; Minimal respiratory and cardiovascular effects",
        "administration_routes": ["IV", "IM"],
        "notes": "يستخدم كمخدر موضعي ومرخي عضلات للقلب في بعض الحالات.",
        "contraindications": "حساسية لأدوية الأميد؛ اضطرابات القلب الخطيرة.",
        "image_path": "images/Lidocaine.png"
    },
    "Bupivacaine": {
        "dose_range_mg_per_kg": [1.5, 2.5],
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IM"],
        "notes": "مخدر موضعي طويل الأمد، يُستخدم في العمليات الجراحية.",
        "contraindications": "حساسية لأدوية الأميد؛ أمراض القلب الشديدة.",
        "image_path": "images/Bupivacaine.png"
    },
    "Fentanyl": {
        "dose_range_mcg_per_kg": [1, 2],
        "side_effects": "Analgesic effects; Depresses respiration; Minimal cardiovascular effects",
        "administration_routes": ["IV", "IM"],
        "notes": "مسكن قوي يستخدم في التخدير وطب العناية المركزة.",
        "contraindications": "الحساسية للأفيونات؛ أمراض الجهاز التنفسي الحادة.",
        "image_path": "images/Fentanyl.png"
    },
    "Remifentanil": {
        "dose_range_mcg_per_kg_per_min": [0.1, 0.3],
        "side_effects": "Analgesic effects; Depresses respiration; Minimal cardiovascular effects",
        "administration_routes": ["IV"],
        "notes": "مسكن سريع المفعول مع مدة تأثير قصيرة، مناسب للجراحات القصيرة.",
        "contraindications": "حساسية للأفيونات؛ أمراض التنفس.",
        "image_path": "images/Remifentanil.png"
    },
    "Morphine": {
        "dose_range_mg_per_kg": [0.05, 0.1],
        "side_effects": "Analgesic effects; Depresses respiration; Decreases BP",
        "administration_routes": ["IV", "IM"],
        "notes": "مسكن أفيوني تقليدي، يستخدم للألم الشديد.",
        "contraindications": "الحساسية للأفيونات؛ حالات الربو الشديدة.",
        "image_path": "images/Morphine.png"
    },
    "Succinylcholine": {
        "dose_range_mg_per_kg": [1, 2],
        "side_effects": "Depresses respiration; Minimal cardiovascular effects",
        "administration_routes": ["IV", "IM"],
        "notes": "يستخدم كمحبس عصبي لتسهيل التنبيب السريع.",
        "contraindications": "فرط بوتاسيوم الدم؛ إصابات حادة في الحبل الشوكي.",
        "image_path": "images/Succinylcholine.png"
    },
    "Rocuronium": {
        "dose_range_mg_per_kg": [0.6, 1.2],
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "notes": "مادة حاصرة لعضلات غير استقطابية، تستخدم للتنبيب السريع.",
        "contraindications": "حساسية؛ أمراض العضلات النادرة.",
        "image_path": "images/Rocuronium.png"
    },
    "Atracurium": {
        "dose_range_mg_per_kg": [0.4, 0.6],
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "notes": "مادة حاصرة لعضلات تستخدم بشكل واسع في التخدير العام.",
        "contraindications": "حساسية؛ أمراض العضلات.",
        "image_path": "images/Atracurium.png"
    },
    "Pancuronium": {
        "dose_range_mg_per_kg": [0.04, 0.1],
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "notes": "مادة حاصرة للعضلات ذات تأثير طويل الأمد.",
        "contraindications": "حساسية؛ اضطرابات القلب.",
        "image_path": "images/Pancuronium.png"
    },
    "Cisatracurium": {
        "dose_range_mg_per_kg": [0.1, 0.2],
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "notes": "مادة حاصرة للعضلات تحظى بشعبية في العناية المركزة بسبب تحللها الآمن.",
        "contraindications": "حساسية.",
        "image_path": "images/Cisatracurium.png"
    },
    "Mivacurium": {
        "dose_range_mg_per_kg": [0.15, 0.2],
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "notes": "حاصرة عضلات ذات مدة قصيرة، تستخدم في الإجراءات السريعة.",
        "contraindications": "حساسية.",
        "image_path": "images/Mivacurium.png"
    },
    "Atropine": {
        "dose_range_mg_per_kg": [0.01, 0.02],
        "side_effects": "Increases heart rate; Decreases secretions",
        "administration_routes": ["IV", "IM", "SC"],
        "notes": "مضاد للكولين يستخدم لزيادة معدل ضربات القلب وتقليل الإفرازات.",
        "contraindications": "زرق؛ تضخم البروستاتا.",
        "image_path": "images/Atropine.png"
    },
    "Glycopyrrolate": {
        "dose_range_mg_per_kg": [0.004, 0.004],
        "side_effects": "Increases heart rate; Decreases secretions",
        "administration_routes": ["IV", "IM", "SC"],
        "notes": "مضاد للكولين مع تأثير طويل الأمد مقارنة بالأتروبين.",
        "contraindications": "زرق؛ أمراض القلب.",
        "image_path": "images/Glycopyrrolate.png"
    },
    "Neostigmine": {
        "dose_range_mg_per_kg": [0.03, 0.07],
        "side_effects": "Reverses neuromuscular block",
        "administration_routes": ["IV"],
        "notes": "مستخدم لعكس تأثيرات حاصرات العضلات.",
        "contraindications": "انسداد الأمعاء؛ الربو.",
        "image_path": "images/Neostigmine.png"
    },
    "Sugammadex": {
        "dose_range_mg_per_kg": [2, 16],
        "side_effects": "Reverses rocuronium and vecuronium",
        "administration_routes": ["IV"],
        "notes": "مادة متخصصة لعكس تأثيرات روكورونيوم وفكورو نيوم.",
        "contraindications": "حساسية للدواء.",
        "image_path": "images/Sugammadex.png"
    }
}


syringes = {
    5: "images/5.png",
    10: "images/10.png",
    20: "images/5.png",
    50: "images/50.png",
}

def calculate_dose(weight, dose_range):
    min_dose = weight * dose_range[0]
    max_dose = weight * dose_range[1]
    return min_dose, max_dose

def recommend_syringe(volume_cc):
    if volume_cc <= 5:
        return 5
    elif volume_cc <= 10:
        return 10
    elif volume_cc <= 20:
        return 20
    else:
        return 50

def show_results_window(drug_name, weight):
    if drug_name not in drugs:
        messagebox.showerror("خطأ", "الدواء غير موجود في القاعدة")
        return

    drug = drugs[drug_name]
    min_dose, max_dose = calculate_dose(weight, drug["dose_range_mg_per_kg"])
    avg_dose = (min_dose + max_dose) / 2
    
    # افتراض: لترطيب/تخفيف، 1 مل ماء مقطر لكل 10 ملغ دواء (تعديل حسب الحاجة)
    dilution_cc = avg_dose / 10
    
    syringe_size = recommend_syringe(dilution_cc)

    results_win = tk.Toplevel()
    results_win.title("نتيجة حساب الجرعة")
    results_win.geometry("600x700")
    results_win.configure(bg="#e6f0ff")

    # تحميل صورة الدواء
    try:
        drug_img = Image.open(drug["image_path"]).resize((150, 150))
        drug_photo = ImageTk.PhotoImage(drug_img)
    except:
        drug_photo = None

    # تحميل صورة السرنجة
    try:
        syringe_img = Image.open(syringes[syringe_size]).resize((120, 120))
        syringe_photo = ImageTk.PhotoImage(syringe_img)
    except:
        syringe_photo = None

    # رأس الصفحة: اسم الدواء وصورته
    header_frame = tk.Frame(results_win, bg="#e6f0ff")
    header_frame.pack(pady=10)
    tk.Label(header_frame, text=f"الدواء: {drug_name}", font=("Arial", 20, "bold"), bg="#e6f0ff").pack()
    if drug_photo:
        tk.Label(header_frame, image=drug_photo, bg="#e6f0ff").pack(pady=5)
    else:
        tk.Label(header_frame, text="صورة الدواء غير متوفرة", bg="#e6f0ff").pack()

    # الجرعة الموصى بها
    tk.Label(results_win, text=f"الجرعة الموصى بها:\nمن {min_dose:.2f} ملغ إلى {max_dose:.2f} ملغ", 
             font=("Arial", 14), bg="#e6f0ff").pack(pady=10)

    # كمية الماء المقطر المطلوبة للتخفيف
    tk.Label(results_win, text=f"كمية الماء المقطر المطلوبة للتخفيف:\n{dilution_cc:.2f} مل", 
             font=("Arial", 14), bg="#e6f0ff").pack(pady=10)

    # السرنجة المناسبة وحجمها + صورتها
    syringe_frame = tk.Frame(results_win, bg="#e6f0ff")
    syringe_frame.pack(pady=10)
    tk.Label(syringe_frame, text=f"حجم السرنجة المستخدمة: {syringe_size} مل", 
             font=("Arial", 14), bg="#e6f0ff").pack()
    if syringe_photo:
        tk.Label(syringe_frame, image=syringe_photo, bg="#e6f0ff").pack(pady=5)
    else:
        tk.Label(syringe_frame, text="صورة السرنجة غير متوفرة", bg="#e6f0ff").pack()

    # موانع الاستعمال
    tk.Label(results_win, text=f"موانع الاستعمال:\n{drug.get('contraindications', '-')}", 
             font=("Arial", 14), bg="#e6f0ff", wraplength=550).pack(pady=10)

    # الآثار الجانبية المحتملة
    tk.Label(results_win, text=f"الآثار الجانبية المحتملة:\n{drug['side_effects']}", 
             font=("Arial", 14), bg="#e6f0ff", wraplength=550).pack(pady=10)

    # مكان الإعطاء
    routes = ", ".join(drug["administration_routes"])
    tk.Label(results_win, text=f"مكان الإعطاء: {routes}", 
             font=("Arial", 14), bg="#e6f0ff").pack(pady=10)

    # ملاحظات
    tk.Label(results_win, text=f"ملاحظات:\n{drug['notes']}", 
             font=("Arial", 14), bg="#e6f0ff", wraplength=550).pack(pady=10)

    # الاحتفاظ بالصور في الذاكرة
    results_win.drug_photo = drug_photo
    results_win.syringe_photo = syringe_photo

def on_calculate():
    try:
        weight = float(weight_entry.get())
        drug_name = drug_var.get()
        if weight <= 0:
            messagebox.showerror("خطأ", "الوزن يجب أن يكون رقم موجب")
            return
        show_results_window(drug_name, weight)
    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال وزن صحيح")

root = tk.Tk()
root.title("حساب جرعات الأدوية")
root.geometry("400x300")
root.configure(bg="#cce0ff")

tk.Label(root, text="اختر الدواء:", font=("Arial", 14), bg="#cce0ff").pack(pady=10)

drug_var = tk.StringVar()
drug_choices = list(drugs.keys())
drug_menu = ttk.Combobox(root, textvariable=drug_var, values=drug_choices, state="readonly")
drug_menu.pack()

tk.Label(root, text="ادخل وزن المريض (كغم):", font=("Arial", 14), bg="#cce0ff").pack(pady=10)
weight_entry = tk.Entry(root)
weight_entry.pack()

calc_button = tk.Button(root, text="حساب الجرعة", command=on_calculate, bg="#3366cc", fg="white", font=("Arial", 12, "bold"))
calc_button.pack(pady=20)

root.mainloop()
