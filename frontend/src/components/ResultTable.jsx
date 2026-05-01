export default function ResultTable({ tests }) {
  return (
    <div>
      <h2>Test Results</h2>
      <table>
        <thead>
          <tr>
            <th>Test</th>
            <th>Value</th>
            <th>Range</th>
            <th>Status</th>
            <th>Explanation</th>
          </tr>
        </thead>
        <tbody>
          {tests.map((test, index) => (
            <tr key={index} className={test.status.toLowerCase()}>
              <td>{test.name}</td>
              <td>{test.value} {test.unit}</td>
              <td>{test.normal_range}</td>
              <td>{test.status}</td>
              <td>{test.explanation}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}