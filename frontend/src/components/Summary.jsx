export default function Summary({ data }) {
  return (
    <div className="summary">
      <h2>Overall Analysis</h2>
      <p>{data.overall_analysis}</p>

      <h3>Recommendations</h3>
      <ul>
        {data.recommendations.map((rec, i) => (
          <li key={i}>{rec}</li>
        ))}
      </ul>
    </div>
  );
}