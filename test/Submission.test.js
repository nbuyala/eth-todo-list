const Submission = artifacts.require('./Submission.sol')

contract('Submission', (account) => {
	before(async () => {
		this.submission = await Submission.deployed()
	})

	it('deploys successfully', async () => {
		const address = await this.submission.address

		assert.notEqual(address, 0x0)
		assert.notEqual(address, '')
		assert.notEqual(address, null)
		assert.notEqual(address, undefined)
	})

	it('list crop', async () => {
		const crop = await this.submission.crops(0)
		assert.equal(crop.name, "mango")
		assert.equal(crop.quantity, 12)
		assert.equal(crop.quality, 35)

	});
})