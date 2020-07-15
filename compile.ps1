# Dereference script path
$dir = $PSScriptRoot;

# Compile all of the jsons 
python "$dir/fmt_compile.py";

# Force copy the output to the correct dir
Copy-Item -Force "$dir/out/*" "$dir/../vgc/"

# Wait for user confirm before close
pause;