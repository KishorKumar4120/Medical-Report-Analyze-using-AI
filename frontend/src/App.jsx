import { useState } from "react";
import UploadForm from "./components/UploadForm";
import ResultTable from "./components/ResultTable";
import Summary from "./components/Summary";
import "./styles.css";

function App() {
  const [data, setData] = useState(null);

  return (
    <div className="container">
      <h1>🧪 Medical Report Analyzer</h1>

      <UploadForm onResult={setData} />

      {data && (
        <>
          <Summary data={data} />
          <ResultTable tests={data.tests} />
        </>
      )}
    </div>
  );
}

export default App;