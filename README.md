### **Steps to Run the Project:**

1. **Complete FHR Onboarding** – Refer to *FHR Onboarding.pdf* for detailed instructions.  
2. **Obtain Hospital VPN Access** – Ensure you have access and are connected.  
3. **Install Dependencies** – Run the following command to install required packages:  
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Script** – Execute:  
   ```bash
   python main.py
   ```
5. **Provide Input** – Enter the required `mother_encounter_id` when prompted.  
6. **Output Files** – Two CSV files will be generated, each containing extracted attributes:
   - **Admission attributes** (prefixed with *adm*)
   - **Delivery attributes** (prefixed with *dlv*)  
   Each file includes the **encounter ID** and the **title of the note** from which attributes were extracted.  
7. **Reference Documentation** – See *FHR.pdf* for design details.
