all: test

test:
	ptw --onpass "say passed" --onfail "say failed" \
	    --runner "pytest --maxfail=5 --ff" \
	#--runner "pytest --testmon" \

debug:
	ptw --onpass "say passed" --onfail "say failed" \
	--runner "pytest --testmon" \
	--pdb
