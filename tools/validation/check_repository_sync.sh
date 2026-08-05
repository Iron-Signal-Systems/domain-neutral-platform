#!/usr/bin/env bash
set -Eeuo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]:-$0}")" && pwd -P)"
python3 "${script_dir}/check_repository_sync.py"
python3 "${script_dir}/check_current_domain_neutrality.py"
exec python3 "${script_dir}/check_project_status.py"
