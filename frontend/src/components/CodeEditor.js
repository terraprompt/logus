import React from 'react';
import AceEditor from 'react-ace';
import 'ace-builds/src-noconflict/mode-text';
import 'ace-builds/src-noconflict/theme-monokai';

const CodeEditor = ({ value, onChange, analysis }) => {
  // Implement custom markers based on analysis
  const markers = analysis?.fragments.map((fragment, index) => ({
    startRow: 0, // You'll need to calculate these based on fragment positions
    startCol: 0,
    endRow: 0,
    endCol: 0,
    className: `fragment-${fragment.type}`,
    type: 'background'
  })) || [];

  return (
    <AceEditor
      mode="text"
      theme="monokai"
      onChange={onChange}
      value={value}
      name="prompt-editor"
      editorProps={{ $blockScrolling: true }}
      setOptions={{
        showLineNumbers: true,
        tabSize: 2,
      }}
      markers={markers}
      style={{ width: '100%', height: '400px' }}
    />
  );
};

export default CodeEditor;