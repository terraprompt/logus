import React from 'react';

const Sidebar = ({ model, setModel, analysis }) => {
  return (
    <div className="w-64 bg-base-300 p-4">
      <select className="select select-bordered w-full" value={model} onChange={e => setModel(e.target.value)}>
        <option value="claude-3-opus-20240229">Claude 3 Opus</option>
        <option value="gpt-4">GPT-4</option>
        <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
        <option value="mixtral-8x7b-32768">Mixtral 8x7B</option>
      </select>
      {analysis && (
        <div className="mt-4">
          <h3 className="text-lg font-semibold">Analysis</h3>
          <p>Goal Alignment: {analysis.overall_goal_alignment}/10</p>
          <p>Effectiveness: {analysis.estimated_effectiveness}/10</p>
          <h4 className="mt-2 font-semibold">Suggested Improvements:</h4>
          <ul className="list-disc pl-4">
            {analysis.suggested_improvements.map((improvement, index) => (
              <li key={index}>{improvement}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Sidebar;