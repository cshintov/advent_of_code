all: test

test:
	cd ${problem} && ptw --onpass "say passed" --onfail "say failed" \
	    --runner "pytest --maxfail=5 --ff -s" \
	#--runner "pytest --testmon" \

debug:
	cd ${problem} && ptw --onpass "say passed" --onfail "say failed" \
	--runner "pytest --testmon" \
	--pdb

new:
	bash ./bin/new.sh ${problem}
