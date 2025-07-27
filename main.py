from ExDoc.headerextractor import headerExtractor
from ExDoc.headerclassifier import HeaderClassifier
import pathlib
import json
inputdir = pathlib.Path("./input")
outputdir = pathlib.Path("./output")
pdfs = [ pdf for pdf in inputdir.glob("*.pdf")]
classifier = HeaderClassifier()
for pdf in pdfs:
    json_path = outputdir / (pdf.stem + ".json")
    predictions_df = classifier.predict_headers(pdf)
    predictions_df.rename(columns={'predicted_label':'level'},inplace=True)
    outline = predictions_df[predictions_df['level']!='other'].loc[:,["level","text","page"]].to_dict(orient="records")
    title = (predictions_df[(predictions_df['page']==0) & ((predictions_df['level']=='H1')|(predictions_df['level']=='H2'))].iloc[0])['text']
    data={"title":title,"outline":outline}
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
