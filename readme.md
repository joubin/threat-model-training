## Requirements

1. `brew install rust`
   1. This is needed by several packages that will be fetched by pip
2. python -m venv venv
3.
4. requirements.txt

## Example Attacks

This section is used to orient the training and set the mental model for the day. Ideally, one or more of these will be used to drive the breach example. 

1. **Yahoo Data Breach (2013-2014)**
   - **Anatomy of Attack:** Hackers gained access to Yahoo's network and compromised all three billion accounts hosted by the service.
   - **STRIDE Classification:** Information Disclosure (user data exposed)
   - **Reference:** [Yahoo 2013 Breach](https://www.reuters.com/article/us-yahoo-cyber/yahoo-says-all-three-billion-accounts-hacked-in-2013-data-theft-idUSKCN1C82O1)

2. **Equifax Data Breach (2017)**
   - **Anatomy of Attack:** Exploited a vulnerability in Apache Struts to access personal information of approximately 147 million people.
   - **STRIDE Classification:** Information Disclosure
   - **Reference:** [Equifax Breach Details](https://www.consumer.ftc.gov/blog/2017/09/equifax-data-breach-what-do)

3. **WannaCry Ransomware Attack (2017)**
   - **Anatomy of Attack:** Exploited the EternalBlue vulnerability in Windows systems for ransomware deployment.
   - **STRIDE Classification:** Denial of Service
   - **Reference:** [WannaCry Ransomware Information](https://www.cisa.gov/uscert/ncas/alerts/TA17-132A)

4. **Capital One Data Breach (2019)**
   - **Anatomy of Attack:** Misconfiguration of a Web Application Firewall allowed unauthorized access to credit card applications.
   - **STRIDE Classification:** Elevation of Privilege
   - **Reference:** [Capital One Breach Explained](https://www.cnbc.com/2019/07/30/capital-one-breach-customer-records-social-security-numbers.html)

5. **SolarWinds Supply Chain Attack (2020)**
   - **Anatomy of Attack:** Malicious code was inserted into the SolarWinds Orion software, affecting thousands of government and private networks.
   - **STRIDE Classification:** Elevation of Privilege
   - **Reference:** [SolarWinds Attack Overview](https://www.csoonline.com/article/573077/solarwinds-creates-new-software-build-system-in-wake-of-sunburst-attack.html)

6. **Colonial Pipeline Ransomware Attack (2021)**
   - **Anatomy of Attack:** Ransomware was used to shut down the pipeline operations, leading to widespread fuel shortages.
   - **STRIDE Classification:** Denial of Service
   - **Reference:** [Colonial Pipeline Incident](https://www.bbc.com/news/business-57050690)

7. **Facebook Data Leak (2019)**
   - **Anatomy of Attack:** Personal data of over 530 million users was exposed due to a vulnerability.
   - **STRIDE Classification:** Information Disclosure
   - **Reference:** [Facebook 2019 Leak](https://www.businessinsider.com/stolen-data-of-533-million-facebook-users-leaked-online-2021-4)

8. **Marriott International Data Breach (2018)**
   - **Anatomy of Attack:** Unauthorized access to the reservation system led to the exposure of information on up to 383 million guests.
   - **STRIDE Classification:** Information Disclosure
   - **Reference:** [Marriott Breach Analysis](https://www.bbc.com/news/technology-46401890)

9. **Adobe Data Breach (2013)**
   - **Anatomy of Attack:** Hackers accessed customer IDs, encrypted passwords, and source code for numerous Adobe products.
   - **STRIDE Classification:** Information Disclosure
   - **Reference:** [Adobe 2013 Breach](https://www.csoonline.com/article/565054/adobe-s-cso-talks-security-the-2013-breach-and-how-he-sets-priorities.html)

10. **JPMorgan Chase Data Breach (2014)**
    - **Anatomy of Attack:** Compromised information of over 83 million households and small businesses.
    - **STRIDE Classification:** Information Disclosure
    - **Reference:** [JPMorgan Chase Breach Details](https://www.reuters.com/article/idUSKCN0HR23T/)

