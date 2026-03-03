// ArticleRow.jsx — Day 62, v4.24
// Single news article row for Context Tab Column C

function scoreBadgeClass(score) {
  if (score > 0.15) return 'bg-green-800/70 text-green-200';
  if (score < -0.15) return 'bg-red-800/70 text-red-200';
  return 'bg-gray-700 text-gray-400';
}

export default function ArticleRow({ emoji, title, url, source, date, score }) {
  return (
    <div className="flex items-start gap-2 py-2 border-b border-gray-700/50 last:border-0">
      <span className="text-base flex-shrink-0 mt-0.5">{emoji}</span>
      <div className="flex-1 min-w-0">
        <a
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-400 hover:text-blue-300 text-xs leading-snug line-clamp-2"
        >
          {title}
        </a>
        <div className="text-gray-600 text-xs mt-0.5">
          {source} · {date}
        </div>
      </div>
      <span className={`text-xs font-mono px-1.5 py-0.5 rounded flex-shrink-0 ${scoreBadgeClass(score)}`}>
        {score > 0 ? '+' : ''}{score?.toFixed(2) ?? '—'}
      </span>
    </div>
  );
}
