import tkinter as tk
from tkinter import ttk, messagebox
import re
drugs = {
    "Propofol": {
        "dose_type": "weight",
        "pediatric_dose": "1-2.5 mg/kg",
        "adult_dose": "1.5-2.5 mg/kg",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Sedation; Depresses respiration; Decreases BP",
        "administration_routes": ["IV"],
        "chemical_compound": "2,6-diisopropylphenol",
        "notes": "N"
    },
    "Ketamine": {
        "dose_type": "weight",
        "pediatric_dose": "1-2 mg/kg (IV)",
        "adult_dose": "4-6 mg/kg (IM)",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Stimulates nervous system; Maintains respiration; Increases BP",
        "administration_routes": ["IV", "IM"],
        "chemical_compound": "Arylcyclohexylamine",
        "notes": "N"
    },
    "Etomidate": {
        "dose_type": "weight",
        "pediatric_dose": "0.2-0.4 mg/kg",
        "adult_dose": "0.2-0.6 mg/kg",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Sedation; Depresses respiration; Stable BP",
        "administration_routes": ["IV"],
        "chemical_compound": "Carboxylated imidazole",
        "notes": "N"
    },
    "Thiopental": {
        "dose_type": "weight",
        "pediatric_dose": "3-5 mg/kg",
        "adult_dose": "3-5 mg/kg",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Sedation; Depresses respiration; Decreases BP",
        "administration_routes": ["IV"],
        "chemical_compound": "Barbiturate",
        "notes": "N"
    },
    "Midazolam": {
        "dose_type": "weight",
        "pediatric_dose": "0.05-0.1 mg/kg",
        "adult_dose": "1-2.5 mg",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Sedation; Amnesia; Minimal respiratory and cardiovascular effects",
        "administration_routes": ["IV", "IM"],
        "chemical_compound": "Benzodiazepine",
        "notes": "N"
    },
    "Dexmedetomidine": {
        "dose_type": "weight/hr",
        "pediatric_dose": "0.2-0.7 mcg/kg/hr",
        "adult_dose": "0.2-1 mcg/kg/hr",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Sedation; Maintains respiration; Stable BP",
        "administration_routes": ["IV"],
        "chemical_compound": "Imidazole derivative",
        "notes": "N"
    },
    "Lidocaine": {
        "dose_type": "weight",
        "pediatric_dose": "0.5-1 mg/kg",
        "adult_dose": "50-100 mg",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Analgesic effects; Minimal respiratory and cardiovascular effects",
        "administration_routes": ["IV", "IM"],
        "chemical_compound": "Amide",
        "notes": "N"
    },
    "Bupivacaine": {
        "dose_type": "weight",
        "pediatric_dose": "1-2 mg/kg",
        "adult_dose": "1.5-2.5 mg/kg",
        "icu_dose": "N/A",
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IM"],
        "chemical_compound": "Amide",
        "notes": "Local anesthesia"
    },
    "Fentanyl": {
        "dose_type": "weight",
        "pediatric_dose": "1-2 mcg/kg",
        "adult_dose": "25-100 mcg",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Analgesic effects; Depresses respiration; Minimal cardiovascular effects",
        "administration_routes": ["IV", "IM"],
        "chemical_compound": "Opioid",
        "notes": "N"
    },
    "Remifentanil": {
        "dose_type": "weight/min",
        "pediatric_dose": "0.05-0.2 mcg/kg/min",
        "adult_dose": "0.1-0.3 mcg/kg/min",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Analgesic effects; Depresses respiration; Minimal cardiovascular effects",
        "administration_routes": ["IV"],
        "chemical_compound": "Opioid",
        "notes": "N"
    },
    "Morphine": {
        "dose_type": "weight",
        "pediatric_dose": "0.05-0.1 mg/kg",
        "adult_dose": "2-10 mg",
        "icu_dose": "Adjusted for sedation",
        "side_effects": "Analgesic effects; Depresses respiration; Decreases BP",
        "administration_routes": ["IV", "IM"],
        "chemical_compound": "Opioid",
        "notes": "N"
    },
    "Succinylcholine": {
        "dose_type": "weight",
        "pediatric_dose": "1-2 mg/kg (IV)",
        "adult_dose": "2-3 mg/kg (IM)",
        "icu_dose": "N/A",
        "side_effects": "Depresses respiration; Minimal cardiovascular effects",
        "administration_routes": ["IV", "IM"],
        "chemical_compound": "Depolarizing agent",
        "notes": "N"
    },
    "Rocuronium": {
        "dose_type": "weight",
        "pediatric_dose": "0.6-1 mg/kg",
        "adult_dose": "0.6-1.2 mg/kg",
        "icu_dose": "N/A",
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "chemical_compound": "Non-depolarizing agent",
        "notes": "Neuromuscular block"
    },
    "Atracurium": {
        "dose_type": "weight",
        "pediatric_dose": "0.4-0.5 mg/kg",
        "adult_dose": "0.4-0.6 mg/kg",
        "icu_dose": "N/A",
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "chemical_compound": "Non-depolarizing agent",
        "notes": "Neuromuscular block"
    },
    "Pancuronium": {
        "dose_type": "weight",
        "pediatric_dose": "0.06-0.1 mg/kg",
        "adult_dose": "0.04-0.1 mg/kg",
        "icu_dose": "N/A",
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "chemical_compound": "Non-depolarizing agent",
        "notes": "Neuromuscular block"
    },
    "Cisatracurium": {
        "dose_type": "weight",
        "pediatric_dose": "0.1-0.15 mg/kg",
        "adult_dose": "0.1-0.2 mg/kg",
        "icu_dose": "N/A",
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "chemical_compound": "Non-depolarizing agent",
        "notes": "Neuromuscular block"
    },
    "Mivacurium": {
        "dose_type": "weight",
        "pediatric_dose": "0.15-0.2 mg/kg",
        "adult_dose": "0.15-0.2 mg/kg",
        "icu_dose": "N/A",
        "side_effects": "Minimal systemic effects",
        "administration_routes": ["IV"],
        "chemical_compound": "Non-depolarizing agent",
        "notes": "Neuromuscular block"
    },
    "Atropine": {
        "dose_type": "weight",
        "pediatric_dose": "0.01-0.02 mg/kg",
        "adult_dose": "0.4-1 mg",
        "icu_dose": "N/A",
        "side_effects": "Increases heart rate; Decreases secretions",
        "administration_routes": ["IV", "IM", "SC"],
        "chemical_compound": "Anticholinergic",
        "notes": "N"
    },
    "Glycopyrrolate": {
        "dose_type": "weight",
        "pediatric_dose": "0.004 mg/kg",
        "adult_dose": "0.1-0.2 mg",
        "icu_dose": "N/A",
        "side_effects": "Increases heart rate; Decreases secretions",
        "administration_routes": ["IV", "IM", "SC"],
        "chemical_compound": "Anticholinergic",
        "notes": "N"
    },
    "Neostigmine": {
        "dose_type": "weight",
        "pediatric_dose": "0.04-0.08 mg/kg",
        "adult_dose": "0.03-0.07 mg/kg",
        "icu_dose": "N/A",
        "side_effects": "Reverses neuromuscular block",
        "administration_routes": ["IV"],
        "chemical_compound": "Acetylcholinesterase inhibitor",
        "notes": "N"
    },
    "Sugammadex": {
        "dose_type": "weight",
        "pediatric_dose": "2-4 mg/kg",
        "adult_dose": "2-16 mg/kg",
        "icu_dose": "N/A",
        "side_effects": "Reverses rocuronium and vecuronium",
        "administration_routes": ["IV"],
        "chemical_compound": "Cyclodextrin derivative",
        "notes": "N"
    },
}


def parse_dose_range(dose_str):
    dose_str = dose_str.strip()
    match = re.match(r"([\d\.]+)-([\d\.]+)\s*(\w*/?kg)?", dose_str)
    if match:
        min_dose = float(match.group(1))
        max_dose = float(match.group(2))
        unit = match.group(3) if match.group(3) else ""
        per_kg = 'kg' in unit
        return min_dose, max_dose, unit.replace("/kg", ""), per_kg
    else:
        return None

def calculate_dose(weight, dose_str):
    parsed = parse_dose_range(dose_str)
    if not parsed:
        return dose_str
    min_dose, max_dose, unit, per_kg = parsed
    if per_kg:
        min_total = min_dose * weight
        max_total = max_dose * weight
    else:
        min_total = min_dose
        max_total = max_dose
    return f"{min_total:.2f} - {max_total:.2f} {unit}"

class Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

class DrugSelectionPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(bg="#58BD4A")

        label = tk.Label(self, text="اختر اسم الدواء:", bg="#58BD4A", fg="#FFFFFF", font=("Arial", 16))
        label.pack(pady=20)

        self.drug_combo = ttk.Combobox(self, values=list(drugs.keys()), state="readonly", font=("Arial", 14))
        self.drug_combo.pack(pady=10)

        next_button = tk.Button(self, text="التالي", bg="#00AAE5", fg="#FFFFFF", font=("Arial", 14, "bold"),
                                command=self.go_next)
        next_button.pack(pady=20)

    def go_next(self):
        if not self.drug_combo.get():
            messagebox.showerror("خطأ", "يرجى اختيار الدواء.")
            return
        self.controller.selected_drug = self.drug_combo.get()
        self.controller.show_frame("WeightOrAgePage")

class WeightOrAgePage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(bg="#7DDD82")

        self.label = tk.Label(self, text="", bg="#50DA5C", fg="#FFFFFF", font=("Arial", 16))
        self.label.pack(pady=20)

        self.entry = tk.Entry(self, font=("Arial", 14))
        self.entry.pack(pady=10)

        button_frame = tk.Frame(self, bg="#6CB84E")
        button_frame.pack(pady=20)

        back_button = tk.Button(button_frame, text="السابق", bg="#00AAE5", fg="#FFFFFF", font=("Arial", 12, "bold"),
                                command=lambda: controller.show_frame("DrugSelectionPage"))
        back_button.grid(row=0, column=0, padx=10)

        next_button = tk.Button(button_frame, text="التالي", bg="#00AAE5", fg="#FFFFFF", font=("Arial", 12, "bold"),
                                command=self.go_next)
        next_button.grid(row=0, column=1, padx=10)

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        drug = self.controller.selected_drug
        dose_type = drugs[drug]["dose_type"]
        if dose_type == "weight":
            self.label.config(text="أدخل وزن المريض (كجم):")
        elif dose_type == "age":
            self.label.config(text="أدخل عمر المريض (سنة):")
        self.entry.delete(0, tk.END)

    def go_next(self):
        value = self.entry.get()
        try:
            val_float = float(value)
            if val_float <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيمة صحيحة موجبة.")
            return
        self.controller.patient_value = val_float
        self.controller.show_frame("DoseInfoPage")

class DoseInfoPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.configure(bg="#BFE459")

        self.text = tk.Text(self, width=50, height=15, font=("Arial", 12), bg="#00008B", fg="#FFFFFF", wrap="word")
        self.text.pack(pady=20)

        button_frame = tk.Frame(self, bg="#CCA72C")
        button_frame.pack(pady=10)

        back_button = tk.Button(button_frame, text="السابق", bg="#00AAE5", fg="#FFFFFF", font=("Arial", 12, "bold"),
                                command=lambda: controller.show_frame("WeightOrAgePage"))
        back_button.grid(row=0, column=0, padx=10)

        finish_button = tk.Button(button_frame, text="إنهاء", bg="#00AAE5", fg="#FFFFFF", font=("Arial", 12, "bold"),
                                  command=self.finish)
        finish_button.grid(row=0, column=1, padx=10)

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        drug = self.controller.selected_drug
        val = self.controller.patient_value
        drug_data = drugs[drug]

        # اختيار الجرعة بناءً على الوزن/العمر والنوع البالغ أو الطفل (نفترض اختيار adult_dose دائمًا هنا لتبسيط)
        # ممكن تضيف اختيار نوع الجرعة مثل pediatric/adult/icu في واجهة إضافية لاحقًا
        dose_type = "adult_dose"
        dose_str = drug_data.get(dose_type, "لا توجد بيانات")

        dose_text = calculate_dose(val, dose_str)

        info_text = (
            f"الدواء: {drug}\n\n"
            f"الجرعة الموصى بها: {dose_text}\n\n"
            f"الآثار الجانبية:\n{drug_data.get('side_effects', 'لا توجد معلومات')}\n\n"
            f"الموانع:\n{drug_data.get('contraindications', 'لا توجد معلومات')}\n\n"
            f"التوصيات عند الاستعمال:\n{drug_data.get('recommendations', 'لا توجد معلومات')}\n\n"
            f"طريقة الإعطاء:\n{drug_data.get('administration', 'لا توجد معلومات')}\n"
        )
        self.text.config(state="normal")
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, info_text)
        self.text.config(state="disabled")

    def finish(self):
        self.controller.destroy()

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("حاسبة الجرعات - 3 صفحات")
        self.geometry("500x500")
        self.configure(bg="#00008B")

        self.selected_drug = None
        self.patient_value = None

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (DrugSelectionPage, WeightOrAgePage, DoseInfoPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("DrugSelectionPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
