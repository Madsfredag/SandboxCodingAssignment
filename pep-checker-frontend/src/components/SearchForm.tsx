import React, { useState } from "react";

interface ISearchFormProps {
  onSearch: (query: string) => void;
}

export function SearchForm({ onSearch }: ISearchFormProps) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) onSearch(query.trim());
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "2rem" }}>
      <input
        type="text"
        placeholder="Search name..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{
          padding: "0.5rem 1rem",
          fontSize: "1rem",
          width: "250px",
          borderRadius: "8px",
          border: "1px solid #ccc",
          marginRight: "1rem",
        }}
      />
      <button
        type="submit"
        style={{
          padding: "0.5rem 1.2rem",
          fontSize: "1rem",
          borderRadius: "8px",
          backgroundColor: "#007acc",
          color: "#fff",
          border: "none",
          cursor: "pointer",
        }}
      >
        Search
      </button>
    </form>
  );
}
