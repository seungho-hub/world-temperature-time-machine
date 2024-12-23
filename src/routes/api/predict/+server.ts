import type { RequestHandler } from '@sveltejs/kit';
import { json } from '@sveltejs/kit';
import { execSync } from 'child_process';

export const GET: RequestHandler = async ({ url }) => {
	const cc = url.searchParams.get('cc')?.toUpperCase();
	const year = url.searchParams.get('year');

	const command = `python src/lib/index.py ${cc} ${year}`;

	const result = execSync(command).toString();

	return json({ prediction: result });
};
