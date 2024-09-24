import React from 'react';

const Analysis = ({ analysis }) => {
  if (!analysis) return null;

  return (
    <div className="bg-base-300 p-4 rounded">
      <h3 className="text-lg font-semibold mb-2">Prompt Analysis</h3>
      <p>Goal Alignment: {analysis.overall_goal_alignment}/10</p>
      <p>Effectiveness: {analysis.estimated_effectiveness}/10</p>
      <h4 className="mt-2 font-semibold">Suggested Improvements:</h4>
      <ul className="list-disc pl-4">
        {analysis.suggested_improvements.map((improvement, index) => (
          <li key={index}>{improvement}</li>
        ))}
      </ul>
    </div>
  );
};

export default Analysis;