import React from 'react';

const ModelSelector = ({ model, setModel }) => {
  return (
    <div className="form-control">
      <label className="label">
        <span className="label-text">Select Model</span>
      </label>
      <select 
        className="select select-bordered w-full" 
        value={model} 
        onChange={e => setModel(e.target.value)}
      >
        <option value="claude-3-opus-20240229">Claude 3 Opus</option>
        <option value="gpt-4">GPT-4</option>
        <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
        <option value="mixtral-8x7b-32768">Mixtral 8x7B</option>
      </select>
    </div>
  );
};

export default ModelSelector;