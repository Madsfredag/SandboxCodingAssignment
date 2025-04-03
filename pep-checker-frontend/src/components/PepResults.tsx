import { PepMatch } from "../api";

interface IPepResultsProps {
  results: PepMatch[];
  hasSearched: boolean;
}

export function PepResults({ results, hasSearched }: IPepResultsProps) {
  if (!hasSearched) return null;
  if (results.length === 0) return <p>No matches found.</p>;

  return (
    <div
      style={{
        maxWidth: "600px",
        marginTop: "2rem",
        display: "grid",
        gap: "1.5rem",
      }}
    >
      {results.map((pep, index) => (
        <div
          key={index}
          style={{
            border: "1px solid #ccc",
            borderRadius: "12px",
            padding: "1rem 1.5rem",
            backgroundColor: "#f4f6f8",
            boxShadow: "0 2px 6px rgba(0,0,0,0.05)",
          }}
        >
          <h2 style={{ margin: 0, fontSize: "1.2rem" }}>{pep.name}</h2>
          <p style={{ margin: "0.4rem 0" }}>
            <strong>Score:</strong> {pep.score.toFixed(2)}
          </p>
          {pep._links?.self?.href && (
            <a
              href={`http://localhost:8000${pep._links.self.href}`}
              target="_blank"
              rel="noreferrer"
              style={{
                color: "#007acc",
                textDecoration: "none",
                fontWeight: 500,
              }}
            >
              View Details →
            </a>
          )}
        </div>
      ))}
    </div>
  );
}
