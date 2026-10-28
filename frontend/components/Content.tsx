type Source = {
  id: number;
  title: string;
  source: string;
};

type ContentProps = {
  category: string;
  question: string;
  sources: Source[];
  content: string;
};

export default function Content({ category, question, sources, content }: ContentProps) {
  return (
    <div className="space-y-4">
      <div>
        <h2>
          Category:
        </h2>
        <p>
          {category}
        </p>
      </div>

      <div>
        <h2>
          Question:
        </h2>
        <p>
          {question}
        </p>
      </div>

      <h2>
        Links:
      </h2>
      <ul>
        {/* Looping through all sources and create a link */}
        {sources.map((source) => (
          <li key={source.id}>
            <a href={source.source}>
              {source.title}
            </a>
          </li>
        ))}
      </ul>

      <h2>
        Content:
      </h2>
      {/* the html link already added as a string from the backend and render here */}
      <div dangerouslySetInnerHTML={{ __html: content }}>
      </div>
    </div>
  );
}
