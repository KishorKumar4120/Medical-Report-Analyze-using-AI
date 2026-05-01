import { useState } from "react";
import { analyzeReport } from "../api";

export default function UploadForm({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Select a file");

    setLoading(true);
    try {
      const result = await analyzeReport(file);
      onResult(result);
      // Reset file state after successful upload
      setFile(null);
    } catch (error) {
      alert("Error analyzing report");
    }
    setLoading(false);
  };

  return (
    <div className="upload-box">
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload}>
        {loading ? "Analyzing..." : "Upload & Analyze"}
      </button>
    </div>
  );
}
