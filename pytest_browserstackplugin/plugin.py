# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack11l1ll11l_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack111ll11ll_opy_, bstack111l1lllll_opy_, update, bstack11llll111l_opy_,
                                       bstack1111l11l1_opy_, bstack1111lll111_opy_, bstack1l11ll1l1_opy_, bstack1l11l1l111_opy_,
                                       bstack1ll111ll1_opy_, bstack111l11l11l_opy_, bstack1l1lll1l11_opy_,
                                       bstack1l1ll1l111_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack11l111l1l1_opy_)
from browserstack_sdk.bstack1lll1ll11_opy_ import bstack11l111ll_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack111ll1ll1l_opy_
from bstack_utils.capture import bstack1lllll11_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack1l1ll11lll_opy_, bstack1llllll1ll_opy_, bstack1lll11ll11_opy_, \
    bstack1lll11ll1l_opy_
from bstack_utils.helper import bstack1l1lllll_opy_, bstack1111l1ll111_opy_, bstack1l1111l1_opy_, bstack11ll1lll11_opy_, bstack1lll1ll1lll_opy_, bstack1l11llll_opy_, \
    bstack1111llll1l1_opy_, \
    bstack111l1111ll1_opy_, bstack1lll1l11l1_opy_, bstack1ll111111l_opy_, bstack111l11lllll_opy_, bstack11l11l11l1_opy_, Notset, \
    bstack1lll11lll1_opy_, bstack111l11l11l1_opy_, bstack111ll1111ll_opy_, Result, bstack1111llll11l_opy_, bstack111l1111l1l_opy_, error_handler, \
    bstack1l1llll11_opy_, bstack1llll111ll_opy_, bstack1l11111l1l_opy_, bstack1111ll1l11l_opy_
from bstack_utils.bstack11l1ll11l11_opy_ import bstack11l1ll111ll_opy_
from bstack_utils.messages import bstack11l1lll11l_opy_, bstack11l11llll_opy_, bstack1ll1lllll_opy_, bstack1l11lll11_opy_, bstack11l11l1l_opy_, \
    bstack1111ll1ll_opy_, bstack11l111l1ll_opy_, bstack1lllll1ll1_opy_, bstack1ll1ll1ll1_opy_, bstack1llll1l1ll_opy_, \
    bstack1ll11ll1ll_opy_, bstack1l11ll11l_opy_, bstack1ll1ll1l11_opy_
from bstack_utils.proxy import bstack1lll11111l_opy_, bstack11ll11l1ll_opy_
from bstack_utils.bstack1ll11lll1_opy_ import bstack11l111ll1ll_opy_, bstack11l111ll11l_opy_, bstack11l11l11l11_opy_, bstack11l11l111l1_opy_, \
    bstack11l111lll1l_opy_, bstack11l11l111ll_opy_, bstack11l11l11111_opy_, bstack11l11l1l1_opy_, bstack11l111llll1_opy_
from bstack_utils.bstack1lll111lll_opy_ import bstack1l111l1ll1_opy_
from bstack_utils.bstack11ll11l1l1_opy_ import bstack1lllll1l1l_opy_, bstack1ll11l1l1l_opy_, bstack1lll1l1lll_opy_, \
    bstack1111ll1l11_opy_, bstack1ll1l11l1_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack1ll1111l_opy_
from bstack_utils.bstack1l1lll11_opy_ import bstack11llll11_opy_
import bstack_utils.accessibility as bstack1lll1ll1l_opy_
from bstack_utils.bstack1llll1ll_opy_ import bstack1l11lll1_opy_
from bstack_utils.bstack11l1l1l1l1_opy_ import bstack11l1l1l1l1_opy_
from bstack_utils.bstack111ll11l_opy_ import bstack1lllll1ll_opy_
from browserstack_sdk.__init__ import bstack1l111111ll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l111ll1l_opy_ import bstack1l1l111l1l1_opy_
from browserstack_sdk.sdk_cli.bstack11llll1lll_opy_ import bstack11llll1lll_opy_, Events, bstack1111lll11_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1ll11111l1l_opy_, bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack11llll1lll_opy_ import bstack11llll1lll_opy_, Events, bstack1111lll11_opy_
bstack1ll1ll111_opy_ = None
bstack11ll1lllll_opy_ = None
bstack1lll11l1l1_opy_ = None
bstack1ll1l111l1_opy_ = None
bstack1lll1ll11l_opy_ = None
bstack11111ll11_opy_ = None
bstack1l1l1ll11_opy_ = None
bstack1ll1ll1l1_opy_ = None
bstack1l1l1l111l_opy_ = None
bstack1lll1l1l1l_opy_ = None
bstack111lll1ll1_opy_ = None
bstack111lll11l1_opy_ = None
bstack1lll111ll1_opy_ = None
bstack11111ll1l_opy_ = bstack11111_opy_ (u"ࠩࠪ≅")
CONFIG = {}
bstack1lll1l1111_opy_ = False
bstack1ll1lllll1_opy_ = bstack11111_opy_ (u"ࠪࠫ≆")
bstack1ll1ll1111_opy_ = bstack11111_opy_ (u"ࠫࠬ≇")
bstack1l1111111l_opy_ = False
bstack1l111ll11_opy_ = []
bstack111lll111_opy_ = bstack1l1ll11lll_opy_
bstack1lll1lllllll_opy_ = bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ≈")
bstack1l11111l1_opy_ = {}
bstack1l111l11ll_opy_ = None
bstack1l1l1llll1_opy_ = False
logger = bstack111ll1ll1l_opy_.get_logger(__name__, bstack111lll111_opy_)
store = {
    bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ≉"): []
}
bstack1lll1lll111l_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1ll1l1ll_opy_ = {}
current_test_uuid = None
cli_context = bstack1ll11111l1l_opy_(
    test_framework_name=bstack1l11111111_opy_[bstack11111_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࠭ࡃࡆࡇࠫ≊")] if bstack11l11l11l1_opy_() else bstack1l11111111_opy_[bstack11111_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࠨ≋")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack11l1lllll1_opy_(page, bstack11ll1llll1_opy_):
    try:
        page.evaluate(bstack11111_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ≌"),
                      bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧ≍") + json.dumps(
                          bstack11ll1llll1_opy_) + bstack11111_opy_ (u"ࠦࢂࢃࠢ≎"))
    except Exception as e:
        print(bstack11111_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿࠥ≏"), e)
def bstack11lllll111_opy_(page, message, level):
    try:
        page.evaluate(bstack11111_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢ≐"), bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ≑") + json.dumps(
            message) + bstack11111_opy_ (u"ࠨ࠮ࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠫ≒") + json.dumps(level) + bstack11111_opy_ (u"ࠩࢀࢁࠬ≓"))
    except Exception as e:
        print(bstack11111_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡿࢂࠨ≔"), e)
def pytest_configure(config):
    global bstack1ll1lllll1_opy_
    global CONFIG
    bstack11l1111l_opy_ = Config.bstack111111ll_opy_()
    config.args = bstack11llll11_opy_.bstack11l11l1ll1l_opy_(config.args)
    bstack11l1111l_opy_.bstack1ll11l11ll_opy_(bstack1l11111l1l_opy_(config.getoption(bstack11111_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ≕"))))
    try:
        bstack111ll1ll1l_opy_.bstack11111l1llll_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack11llll1lll_opy_.invoke(Events.CONNECT, bstack1111lll11_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ≖"), bstack11111_opy_ (u"࠭࠰ࠨ≗")))
        config = json.loads(os.environ.get(bstack11111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࠨ≘"), bstack11111_opy_ (u"ࠣࡽࢀࠦ≙")))
        cli.bstack1l1l1111ll1_opy_(bstack1ll111111l_opy_(bstack1ll1lllll1_opy_, CONFIG), cli_context.platform_index, bstack11llll111l_opy_)
    if cli.bstack1l1l11111l1_opy_(bstack1l1l111l1l1_opy_):
        cli.bstack1l1l11l1111_opy_()
        logger.debug(bstack11111_opy_ (u"ࠤࡆࡐࡎࠦࡩࡴࠢࡤࡧࡹ࡯ࡶࡦࠢࡩࡳࡷࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࠣ≚") + str(cli_context.platform_index) + bstack11111_opy_ (u"ࠥࠦ≛"))
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.BEFORE_ALL, bstack1lll1l1ll11_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack11111_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤ≜"), None)
    if cli.is_running() and when == bstack11111_opy_ (u"ࠧࡩࡡ࡭࡮ࠥ≝"):
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.LOG_REPORT, bstack1lll1l1ll11_opy_.PRE, item, call)
    outcome = yield
    if when == bstack11111_opy_ (u"ࠨࡣࡢ࡮࡯ࠦ≞"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤ≟")))
        if not passed:
            config = json.loads(os.environ.get(bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠢ≠"), bstack11111_opy_ (u"ࠤࡾࢁࠧ≡")))
            if bstack1lllll1ll_opy_.bstack1111l1ll_opy_(config):
                bstack1lllll1ll1ll_opy_ = bstack1lllll1ll_opy_.bstack1111l1l1_opy_(config)
                if item.execution_count > bstack1lllll1ll1ll_opy_:
                    print(bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡳࡧࡷࡶ࡮࡫ࡳ࠻ࠢࠪ≢"), report.nodeid, os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ≣")))
                    bstack1lllll1ll_opy_.bstack11l1111l1l1_opy_(report.nodeid)
            else:
                print(bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࠬ≤"), report.nodeid, os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ≥")))
                bstack1lllll1ll_opy_.bstack11l1111l1l1_opy_(report.nodeid)
        else:
            print(bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࠥࡶࡡࡴࡵࡨࡨ࠿ࠦࠧ≦"), report.nodeid, os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭≧")))
    if cli.is_running():
        if when == bstack11111_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣ≨"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.BEFORE_EACH, bstack1lll1l1ll11_opy_.POST, item, call, outcome)
        elif when == bstack11111_opy_ (u"ࠥࡧࡦࡲ࡬ࠣ≩"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.LOG_REPORT, bstack1lll1l1ll11_opy_.POST, item, call, outcome)
        elif when == bstack11111_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ≪"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.AFTER_EACH, bstack1lll1l1ll11_opy_.POST, item, call, outcome)
        return # skip all existing operations
    skipSessionName = item.config.getoption(bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ≫"))
    plugins = item.config.getoption(bstack11111_opy_ (u"ࠨࡰ࡭ࡷࡪ࡭ࡳࡹࠢ≬"))
    report = outcome.get_result()
    os.environ[bstack11111_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪ≭")] = report.nodeid
    bstack1lll1ll11l1l_opy_(item, call, report)
    if bstack11111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡰ࡭ࡷࡪ࡭ࡳࠨ≮") not in plugins or bstack11l11l11l1_opy_():
        return
    summary = []
    driver = getattr(item, bstack11111_opy_ (u"ࠤࡢࡨࡷ࡯ࡶࡦࡴࠥ≯"), None)
    page = getattr(item, bstack11111_opy_ (u"ࠥࡣࡵࡧࡧࡦࠤ≰"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1lll1llllll1_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1lll1lll1lll_opy_(item, report, summary, skipSessionName)
def bstack1lll1llllll1_opy_(item, report, summary, skipSessionName):
    if report.when == bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ≱") and report.skipped:
        bstack11l111llll1_opy_(report)
    if report.when in [bstack11111_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦ≲"), bstack11111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣ≳")]:
        return
    if not bstack1lll1ll1lll_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack11111_opy_ (u"ࠧࡵࡴࡸࡩࠬ≴")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭≵") + json.dumps(
                    report.nodeid) + bstack11111_opy_ (u"ࠩࢀࢁࠬ≶"))
        os.environ[bstack11111_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭≷")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11111_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࡀࠠࡼ࠲ࢀࠦ≸").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢ≹")))
    bstack1ll11l1ll1_opy_ = bstack11111_opy_ (u"ࠨࠢ≺")
    bstack11l111llll1_opy_(report)
    if not passed:
        try:
            bstack1ll11l1ll1_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11111_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢ≻").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll11l1ll1_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ≼")))
        bstack1ll11l1ll1_opy_ = bstack11111_opy_ (u"ࠤࠥ≽")
        if not passed:
            try:
                bstack1ll11l1ll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11111_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥ≾").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll11l1ll1_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨ≿")
                    + json.dumps(bstack11111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠦࠨ⊀"))
                    + bstack11111_opy_ (u"ࠨ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠤ⊁")
                )
            else:
                item._driver.execute_script(
                    bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡩࡧࡴࡢࠤ࠽ࠤࠬ⊂")
                    + json.dumps(str(bstack1ll11l1ll1_opy_))
                    + bstack11111_opy_ (u"ࠣ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࠦ⊃")
                )
        except Exception as e:
            summary.append(bstack11111_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡢࡰࡱࡳࡹࡧࡴࡦ࠼ࠣࡿ࠵ࢃࠢ⊄").format(e))
def bstack1lll1ll1llll_opy_(test_name, error_message):
    try:
        bstack1llll111l111_opy_ = []
        bstack11l1l1l11l_opy_ = os.environ.get(bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ⊅"), bstack11111_opy_ (u"ࠫ࠵࠭⊆"))
        bstack11ll1l1ll_opy_ = {bstack11111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ⊇"): test_name, bstack11111_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⊈"): error_message, bstack11111_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭⊉"): bstack11l1l1l11l_opy_}
        bstack1llll111l1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠨࡲࡺࡣࡵࡿࡴࡦࡵࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭⊊"))
        if os.path.exists(bstack1llll111l1l1_opy_):
            with open(bstack1llll111l1l1_opy_) as f:
                bstack1llll111l111_opy_ = json.load(f)
        bstack1llll111l111_opy_.append(bstack11ll1l1ll_opy_)
        with open(bstack1llll111l1l1_opy_, bstack11111_opy_ (u"ࠩࡺࠫ⊋")) as f:
            json.dump(bstack1llll111l111_opy_, f)
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡥࡳࡵ࡬ࡷࡹ࡯࡮ࡨࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡰࡺࡶࡨࡷࡹࠦࡥࡳࡴࡲࡶࡸࡀࠠࠨ⊌") + str(e))
def bstack1lll1lll1lll_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack11111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥ⊍"), bstack11111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢ⊎")]:
        return
    if (str(skipSessionName).lower() != bstack11111_opy_ (u"࠭ࡴࡳࡷࡨࠫ⊏")):
        bstack11l1lllll1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤ⊐")))
    bstack1ll11l1ll1_opy_ = bstack11111_opy_ (u"ࠣࠤ⊑")
    bstack11l111llll1_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1ll11l1ll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11111_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤ⊒").format(e)
                )
        try:
            if passed:
                bstack1ll1l11l1_opy_(getattr(item, bstack11111_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩ⊓"), None), bstack11111_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ⊔"))
            else:
                error_message = bstack11111_opy_ (u"ࠬ࠭⊕")
                if bstack1ll11l1ll1_opy_:
                    bstack11lllll111_opy_(item._page, str(bstack1ll11l1ll1_opy_), bstack11111_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧ⊖"))
                    bstack1ll1l11l1_opy_(getattr(item, bstack11111_opy_ (u"ࠧࡠࡲࡤ࡫ࡪ࠭⊗"), None), bstack11111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ⊘"), str(bstack1ll11l1ll1_opy_))
                    error_message = str(bstack1ll11l1ll1_opy_)
                else:
                    bstack1ll1l11l1_opy_(getattr(item, bstack11111_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨ⊙"), None), bstack11111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ⊚"))
                bstack1lll1ll1llll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11111_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀ࠶ࡽࠣ⊛").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack11111_opy_ (u"ࠧ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ⊜"), default=bstack11111_opy_ (u"ࠨࡆࡢ࡮ࡶࡩࠧ⊝"), help=bstack11111_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡪࡥࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠨ⊞"))
    parser.addoption(bstack11111_opy_ (u"ࠣ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ⊟"), default=bstack11111_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣ⊠"), help=bstack11111_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡨࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠤ⊡"))
    parser.addoption(bstack11111_opy_ (u"ࠫ࠲࠳ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭࡯ࡱࡧࡩ࡮ࡪࡳࠨ⊢"), action=bstack11111_opy_ (u"ࠬࡹࡴࡰࡴࡨࡣࡹࡸࡵࡦࠩ⊣"), default=False, help=bstack11111_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࠿ࠦࡃࡰ࡮࡯ࡩࡨࡺࠠࡢࡰࡧࠤࡵࡸࡩ࡯ࡶࠣࡸࡪࡹࡴࠡࡰࡲࡨࡪ࡯ࡤࡴࠢ࡬ࡲࠥࡩ࡬ࡦࡣࡱࠤ࡫ࡵࡲ࡮ࡣࡷ࠰ࠥࡺࡨࡦࡰࠣࡩࡽ࡯ࡴࠨ⊤"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11111_opy_ (u"ࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤ⊥"), action=bstack11111_opy_ (u"ࠣࡵࡷࡳࡷ࡫ࠢ⊦"), default=bstack11111_opy_ (u"ࠤࡦ࡬ࡷࡵ࡭ࡦࠤ⊧"),
                         help=bstack11111_opy_ (u"ࠥࡈࡷ࡯ࡶࡦࡴࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴࠤ⊨"))
def bstack1l1lll1l_opy_(log):
    if not (log[bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⊩")] and log[bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⊪")].strip()):
        return
    active = bstack11lll1l1_opy_()
    log = {
        bstack11111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⊫"): log[bstack11111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⊬")],
        bstack11111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⊭"): bstack1l1111l1_opy_().isoformat() + bstack11111_opy_ (u"ࠩ࡝ࠫ⊮"),
        bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⊯"): log[bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⊰")],
    }
    if active:
        if active[bstack11111_opy_ (u"ࠬࡺࡹࡱࡧࠪ⊱")] == bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⊲"):
            log[bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⊳")] = active[bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⊴")]
        elif active[bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⊵")] == bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࠨ⊶"):
            log[bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⊷")] = active[bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⊸")]
    bstack1l11lll1_opy_.bstack11llllll_opy_([log])
def bstack11lll1l1_opy_():
    if len(store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⊹")]) > 0 and store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⊺")][-1]:
        return {
            bstack11111_opy_ (u"ࠨࡶࡼࡴࡪ࠭⊻"): bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⊼"),
            bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⊽"): store[bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⊾")][-1]
        }
    if store.get(bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ⊿"), None):
        return {
            bstack11111_opy_ (u"࠭ࡴࡺࡲࡨࠫ⋀"): bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࠬ⋁"),
            bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⋂"): store[bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⋃")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.INIT_TEST, bstack1lll1l1ll11_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.INIT_TEST, bstack1lll1l1ll11_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1lll1ll11l11_opy_ = True
        bstack11ll111lll_opy_ = bstack1lll1ll1l_opy_.bstack11l1lllll_opy_(bstack111l1111ll1_opy_(item.own_markers))
        if not cli.bstack1l1l11111l1_opy_(bstack1l1l111l1l1_opy_):
            item._a11y_test_case = bstack11ll111lll_opy_
            if bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ⋄"), None):
                driver = getattr(item, bstack11111_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ⋅"), None)
                item._a11y_started = bstack1lll1ll1l_opy_.bstack1lll1111l1_opy_(driver, bstack11ll111lll_opy_)
        if not bstack1l11lll1_opy_.on() or bstack1lll1lllllll_opy_ != bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ⋆"):
            return
        global current_test_uuid #, bstack1ll1l11l_opy_
        bstack11lll11l_opy_ = {
            bstack11111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⋇"): uuid4().__str__(),
            bstack11111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⋈"): bstack1l1111l1_opy_().isoformat() + bstack11111_opy_ (u"ࠨ࡜ࠪ⋉")
        }
        current_test_uuid = bstack11lll11l_opy_[bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⋊")]
        store[bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⋋")] = bstack11lll11l_opy_[bstack11111_opy_ (u"ࠫࡺࡻࡩࡥࠩ⋌")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1ll1l1ll_opy_[item.nodeid] = {**_1ll1l1ll_opy_[item.nodeid], **bstack11lll11l_opy_}
        bstack1lll1lllll1l_opy_(item, _1ll1l1ll_opy_[item.nodeid], bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⋍"))
    except Exception as err:
        print(bstack11111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡣࡢ࡮࡯࠾ࠥࢁࡽࠨ⋎"), str(err))
def pytest_runtest_setup(item):
    store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⋏")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.BEFORE_EACH, bstack1lll1l1ll11_opy_.PRE, item, bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⋐"))
    if bstack1lllll1ll_opy_.bstack111lll1lll1_opy_():
            bstack1lll1lll1l11_opy_ = bstack11111_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡤࡷࠥࡺࡨࡦࠢࡤࡦࡴࡸࡴࠡࡤࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠨ⋑")
            logger.error(bstack1lll1lll1l11_opy_)
            bstack11lll11l_opy_ = {
                bstack11111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⋒"): uuid4().__str__(),
                bstack11111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⋓"): bstack1l1111l1_opy_().isoformat() + bstack11111_opy_ (u"ࠬࡠࠧ⋔"),
                bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⋕"): bstack1l1111l1_opy_().isoformat() + bstack11111_opy_ (u"࡛ࠧࠩ⋖"),
                bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⋗"): bstack11111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ⋘"),
                bstack11111_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ⋙"): bstack1lll1lll1l11_opy_,
                bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⋚"): [],
                bstack11111_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ⋛"): []
            }
            bstack1lll1lllll1l_opy_(item, bstack11lll11l_opy_, bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧ⋜"))
            pytest.skip(bstack1lll1lll1l11_opy_)
            return # skip all existing operations
    global bstack1lll1lll111l_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111l11lllll_opy_():
        atexit.register(bstack11l1ll1l11_opy_)
        if not bstack1lll1lll111l_opy_:
            try:
                bstack1lll1ll1111l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack1111ll1l11l_opy_():
                    bstack1lll1ll1111l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1ll1111l_opy_:
                    signal.signal(s, bstack1lll1llll1ll_opy_)
                bstack1lll1lll111l_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩ࡬࡯ࡳࡵࡧࡵࠤࡸ࡯ࡧ࡯ࡣ࡯ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶࡸࡀࠠࠣ⋝") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l111ll1ll_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⋞")
    try:
        if not bstack1l11lll1_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack11lll11l_opy_ = {
            bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⋟"): uuid,
            bstack11111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⋠"): bstack1l1111l1_opy_().isoformat() + bstack11111_opy_ (u"ࠫ࡟࠭⋡"),
            bstack11111_opy_ (u"ࠬࡺࡹࡱࡧࠪ⋢"): bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⋣"),
            bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ⋤"): bstack11111_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭⋥"),
            bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬ⋦"): bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ⋧")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ⋨")] = item
        store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⋩")] = [uuid]
        if not _1ll1l1ll_opy_.get(item.nodeid, None):
            _1ll1l1ll_opy_[item.nodeid] = {bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⋪"): [], bstack11111_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⋫"): []}
        _1ll1l1ll_opy_[item.nodeid][bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⋬")].append(bstack11lll11l_opy_[bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⋭")])
        _1ll1l1ll_opy_[item.nodeid + bstack11111_opy_ (u"ࠪ࠱ࡸ࡫ࡴࡶࡲࠪ⋮")] = bstack11lll11l_opy_
        bstack1lll1ll11ll1_opy_(item, bstack11lll11l_opy_, bstack11111_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⋯"))
    except Exception as err:
        print(bstack11111_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨ⋰"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.AFTER_EACH, bstack1lll1l1ll11_opy_.PRE, item, bstack11111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ⋱"))
        return # skip all existing operations
    try:
        global bstack1l11111l1_opy_
        bstack11l1l1l11l_opy_ = 0
        if bstack1l1111111l_opy_ is True:
            bstack11l1l1l11l_opy_ = int(os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ⋲")))
        if bstack111l111ll_opy_.bstack1lll111l1_opy_() == bstack11111_opy_ (u"ࠣࡶࡵࡹࡪࠨ⋳"):
            if bstack111l111ll_opy_.bstack1l11l11ll1_opy_() == bstack11111_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦ⋴"):
                bstack1llll1111lll_opy_ = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⋵"), None)
                bstack1l111lll1_opy_ = bstack1llll1111lll_opy_ + bstack11111_opy_ (u"ࠦ࠲ࡺࡥࡴࡶࡦࡥࡸ࡫ࠢ⋶")
                driver = getattr(item, bstack11111_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭⋷"), None)
                bstack11llll1l1l_opy_ = getattr(item, bstack11111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⋸"), None)
                bstack11111l11ll_opy_ = getattr(item, bstack11111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⋹"), None)
                PercySDK.screenshot(driver, bstack1l111lll1_opy_, bstack11llll1l1l_opy_=bstack11llll1l1l_opy_, bstack11111l11ll_opy_=bstack11111l11ll_opy_, bstack1l1l11l111_opy_=bstack11l1l1l11l_opy_)
        if not cli.bstack1l1l11111l1_opy_(bstack1l1l111l1l1_opy_):
            if getattr(item, bstack11111_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠨ⋺"), False):
                bstack11l111ll_opy_.bstack1lll1llll_opy_(getattr(item, bstack11111_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ⋻"), None), bstack1l11111l1_opy_, logger, item)
        if not bstack1l11lll1_opy_.on():
            return
        bstack11lll11l_opy_ = {
            bstack11111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⋼"): uuid4().__str__(),
            bstack11111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⋽"): bstack1l1111l1_opy_().isoformat() + bstack11111_opy_ (u"ࠬࡠࠧ⋾"),
            bstack11111_opy_ (u"࠭ࡴࡺࡲࡨࠫ⋿"): bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ⌀"),
            bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ⌁"): bstack11111_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭⌂"),
            bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭⌃"): bstack11111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭⌄")
        }
        _1ll1l1ll_opy_[item.nodeid + bstack11111_opy_ (u"ࠬ࠳ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ⌅")] = bstack11lll11l_opy_
        bstack1lll1ll11ll1_opy_(item, bstack11lll11l_opy_, bstack11111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⌆"))
    except Exception as err:
        print(bstack11111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯࠼ࠣࡿࢂ࠭⌇"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l11l111l1_opy_(fixturedef.argname):
        store[bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧ⌈")] = request.node
    elif bstack11l111lll1l_opy_(fixturedef.argname):
        store[bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡧࡱࡧࡳࡴࡡ࡬ࡸࡪࡳࠧ⌉")] = request.node
    if not bstack1l11lll1_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.SETUP_FIXTURE, bstack1lll1l1ll11_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.SETUP_FIXTURE, bstack1lll1l1ll11_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.SETUP_FIXTURE, bstack1lll1l1ll11_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.SETUP_FIXTURE, bstack1lll1l1ll11_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    try:
        fixture = {
            bstack11111_opy_ (u"ࠪࡲࡦࡳࡥࠨ⌊"): fixturedef.argname,
            bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⌋"): bstack1111llll1l1_opy_(outcome),
            bstack11111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⌌"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⌍")]
        if not _1ll1l1ll_opy_.get(current_test_item.nodeid, None):
            _1ll1l1ll_opy_[current_test_item.nodeid] = {bstack11111_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⌎"): []}
        _1ll1l1ll_opy_[current_test_item.nodeid][bstack11111_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ⌏")].append(fixture)
    except Exception as err:
        logger.debug(bstack11111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡶࡩࡹࡻࡰ࠻ࠢࡾࢁࠬ⌐"), str(err))
if bstack11l11l11l1_opy_() and bstack1l11lll1_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.STEP, bstack1lll1l1ll11_opy_.PRE, request, step)
            return
        try:
            _1ll1l1ll_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⌑")].bstack11ll1lll_opy_(id(step))
        except Exception as err:
            print(bstack11111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴ࠿ࠦࡻࡾࠩ⌒"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.STEP, bstack1lll1l1ll11_opy_.POST, request, step, exception)
            return
        try:
            _1ll1l1ll_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ⌓")].bstack1l1l1111_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡶࡸࡪࡶ࡟ࡦࡴࡵࡳࡷࡀࠠࡼࡿࠪ⌔"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.STEP, bstack1lll1l1ll11_opy_.POST, request, step)
            return
        try:
            bstack1ll1ll11_opy_: bstack1ll1111l_opy_ = _1ll1l1ll_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ⌕")]
            bstack1ll1ll11_opy_.bstack1l1l1111_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡸࡺࡥࡱࡡࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠬ⌖"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1lllllll_opy_
        try:
            if not bstack1l11lll1_opy_.on() or bstack1lll1lllllll_opy_ != bstack11111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭⌗"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ⌘"), None)
            if not _1ll1l1ll_opy_.get(request.node.nodeid, None):
                _1ll1l1ll_opy_[request.node.nodeid] = {}
            bstack1ll1ll11_opy_ = bstack1ll1111l_opy_.bstack11111l1111l_opy_(
                scenario, feature, request.node,
                name=bstack11l11l111ll_opy_(request.node, scenario),
                started_at=bstack1l11llll_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11111_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭⌙"),
                tags=bstack11l11l11111_opy_(feature, scenario),
                bstack1lll11ll_opy_=bstack1l11lll1_opy_.bstack1l1l1lll_opy_(driver) if driver and driver.session_id else {}
            )
            _1ll1l1ll_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ⌚")] = bstack1ll1ll11_opy_
            bstack1lll1ll111ll_opy_(bstack1ll1ll11_opy_.uuid)
            bstack1l11lll1_opy_.bstack11llll1l_opy_(bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⌛"), bstack1ll1ll11_opy_)
        except Exception as err:
            print(bstack11111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳ࠿ࠦࡻࡾࠩ⌜"), str(err))
def bstack1lll1lll11l1_opy_(bstack11ll1ll1_opy_):
    if bstack11ll1ll1_opy_ in store[bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⌝")]:
        store[bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⌞")].remove(bstack11ll1ll1_opy_)
def bstack1lll1ll111ll_opy_(test_uuid):
    store[bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⌟")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1l11lll1_opy_.bstack1llll1l1l111_opy_
def bstack1lll1ll11l1l_opy_(item, call, report):
    logger.debug(bstack11111_opy_ (u"ࠫ࡭ࡧ࡮ࡥ࡮ࡨࡣࡴ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡴࡶࡤࡶࡹ࠭⌠"))
    global bstack1lll1lllllll_opy_
    bstack1111l1l11_opy_ = bstack1l11llll_opy_()
    if hasattr(report, bstack11111_opy_ (u"ࠬࡹࡴࡰࡲࠪ⌡")):
        bstack1111l1l11_opy_ = bstack1111llll11l_opy_(report.stop)
    elif hasattr(report, bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࠬ⌢")):
        bstack1111l1l11_opy_ = bstack1111llll11l_opy_(report.start)
    try:
        if getattr(report, bstack11111_opy_ (u"ࠧࡸࡪࡨࡲࠬ⌣"), bstack11111_opy_ (u"ࠨࠩ⌤")) == bstack11111_opy_ (u"ࠩࡦࡥࡱࡲࠧ⌥"):
            logger.debug(bstack11111_opy_ (u"ࠪ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡳࡵࡣࡷࡩࠥ࠳ࠠࡼࡿ࠯ࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠ࠮ࠢࡾࢁࠬ⌦").format(getattr(report, bstack11111_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⌧"), bstack11111_opy_ (u"ࠬ࠭⌨")).__str__(), bstack1lll1lllllll_opy_))
            if bstack1lll1lllllll_opy_ == bstack11111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭〈"):
                _1ll1l1ll_opy_[item.nodeid][bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ〉")] = bstack1111l1l11_opy_
                bstack1lll1lllll1l_opy_(item, _1ll1l1ll_opy_[item.nodeid], bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⌫"), report, call)
                store[bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⌬")] = None
            elif bstack1lll1lllllll_opy_ == bstack11111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢ⌭"):
                bstack1ll1ll11_opy_ = _1ll1l1ll_opy_[item.nodeid][bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⌮")]
                bstack1ll1ll11_opy_.set(hooks=_1ll1l1ll_opy_[item.nodeid].get(bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⌯"), []))
                exception, bstack1l11ll11_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l11ll11_opy_ = [call.excinfo.exconly(), getattr(report, bstack11111_opy_ (u"࠭࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠬ⌰"), bstack11111_opy_ (u"ࠧࠨ⌱"))]
                bstack1ll1ll11_opy_.stop(time=bstack1111l1l11_opy_, result=Result(result=getattr(report, bstack11111_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩ⌲"), bstack11111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⌳")), exception=exception, bstack1l11ll11_opy_=bstack1l11ll11_opy_))
                bstack1l11lll1_opy_.bstack11llll1l_opy_(bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⌴"), _1ll1l1ll_opy_[item.nodeid][bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⌵")])
        elif getattr(report, bstack11111_opy_ (u"ࠬࡽࡨࡦࡰࠪ⌶"), bstack11111_opy_ (u"࠭ࠧ⌷")) in [bstack11111_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⌸"), bstack11111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪ⌹")]:
            logger.debug(bstack11111_opy_ (u"ࠩ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡹࡴࡢࡶࡨࠤ࠲ࠦࡻࡾ࠮ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦ࠭ࠡࡽࢀࠫ⌺").format(getattr(report, bstack11111_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⌻"), bstack11111_opy_ (u"ࠫࠬ⌼")).__str__(), bstack1lll1lllllll_opy_))
            bstack1l1ll1l1_opy_ = item.nodeid + bstack11111_opy_ (u"ࠬ࠳ࠧ⌽") + getattr(report, bstack11111_opy_ (u"࠭ࡷࡩࡧࡱࠫ⌾"), bstack11111_opy_ (u"ࠧࠨ⌿"))
            if getattr(report, bstack11111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ⍀"), False):
                hook_type = bstack11111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧ⍁") if getattr(report, bstack11111_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⍂"), bstack11111_opy_ (u"ࠫࠬ⍃")) == bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ⍄") else bstack11111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ⍅")
                _1ll1l1ll_opy_[bstack1l1ll1l1_opy_] = {
                    bstack11111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⍆"): uuid4().__str__(),
                    bstack11111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⍇"): bstack1111l1l11_opy_,
                    bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬ⍈"): hook_type
                }
            _1ll1l1ll_opy_[bstack1l1ll1l1_opy_][bstack11111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⍉")] = bstack1111l1l11_opy_
            bstack1lll1lll11l1_opy_(_1ll1l1ll_opy_[bstack1l1ll1l1_opy_][bstack11111_opy_ (u"ࠫࡺࡻࡩࡥࠩ⍊")])
            bstack1lll1ll11ll1_opy_(item, _1ll1l1ll_opy_[bstack1l1ll1l1_opy_], bstack11111_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⍋"), report, call)
            if getattr(report, bstack11111_opy_ (u"࠭ࡷࡩࡧࡱࠫ⍌"), bstack11111_opy_ (u"ࠧࠨ⍍")) == bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⍎"):
                if getattr(report, bstack11111_opy_ (u"ࠩࡲࡹࡹࡩ࡯࡮ࡧࠪ⍏"), bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ⍐")) == bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⍑"):
                    bstack11lll11l_opy_ = {
                        bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪ⍒"): uuid4().__str__(),
                        bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⍓"): bstack1l11llll_opy_(),
                        bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⍔"): bstack1l11llll_opy_()
                    }
                    _1ll1l1ll_opy_[item.nodeid] = {**_1ll1l1ll_opy_[item.nodeid], **bstack11lll11l_opy_}
                    bstack1lll1lllll1l_opy_(item, _1ll1l1ll_opy_[item.nodeid], bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⍕"))
                    bstack1lll1lllll1l_opy_(item, _1ll1l1ll_opy_[item.nodeid], bstack11111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⍖"), report, call)
    except Exception as err:
        print(bstack11111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࢁࡽࠨ⍗"), str(err))
def bstack1lll1ll1ll11_opy_(test, bstack11lll11l_opy_, result=None, call=None, bstack1ll1l1l1l_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1ll1ll11_opy_ = {
        bstack11111_opy_ (u"ࠫࡺࡻࡩࡥࠩ⍘"): bstack11lll11l_opy_[bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪ⍙")],
        bstack11111_opy_ (u"࠭ࡴࡺࡲࡨࠫ⍚"): bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࠬ⍛"),
        bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭⍜"): test.name,
        bstack11111_opy_ (u"ࠩࡥࡳࡩࡿࠧ⍝"): {
            bstack11111_opy_ (u"ࠪࡰࡦࡴࡧࠨ⍞"): bstack11111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ⍟"),
            bstack11111_opy_ (u"ࠬࡩ࡯ࡥࡧࠪ⍠"): inspect.getsource(test.obj)
        },
        bstack11111_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ⍡"): test.name,
        bstack11111_opy_ (u"ࠧࡴࡥࡲࡴࡪ࠭⍢"): test.name,
        bstack11111_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨ⍣"): bstack11llll11_opy_.bstack1ll1l111_opy_(test),
        bstack11111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ⍤"): file_path,
        bstack11111_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬ⍥"): file_path,
        bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⍦"): bstack11111_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭⍧"),
        bstack11111_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫ⍨"): file_path,
        bstack11111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⍩"): bstack11lll11l_opy_[bstack11111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⍪")],
        bstack11111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ⍫"): bstack11111_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪ⍬"),
        bstack11111_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳࠧ⍭"): {
            bstack11111_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩ⍮"): test.nodeid
        },
        bstack11111_opy_ (u"࠭ࡴࡢࡩࡶࠫ⍯"): bstack111l1111ll1_opy_(test.own_markers)
    }
    if bstack1ll1l1l1l_opy_ in [bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ⍰"), bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⍱")]:
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠩࡰࡩࡹࡧࠧ⍲")] = {
            bstack11111_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ⍳"): bstack11lll11l_opy_.get(bstack11111_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭⍴"), [])
        }
    if bstack1ll1l1l1l_opy_ == bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭⍵"):
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⍶")] = bstack11111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⍷")
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⍸")] = bstack11lll11l_opy_[bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⍹")]
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⍺")] = bstack11lll11l_opy_[bstack11111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⍻")]
    if result:
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⍼")] = result.outcome
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ⍽")] = result.duration * 1000
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⍾")] = bstack11lll11l_opy_[bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⍿")]
        if result.failed:
            bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ⎀")] = bstack1l11lll1_opy_.bstack111111lll1_opy_(call.excinfo.typename)
            bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ⎁")] = bstack1l11lll1_opy_.bstack1llll1l1lll1_opy_(call.excinfo, result)
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⎂")] = bstack11lll11l_opy_[bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⎃")]
    if outcome:
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⎄")] = bstack1111llll1l1_opy_(outcome)
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ⎅")] = 0
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⎆")] = bstack11lll11l_opy_[bstack11111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⎇")]
        if bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⎈")] == bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⎉"):
            bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ⎊")] = bstack11111_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧ⎋")  # bstack1lll1ll1l111_opy_
            bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ⎌")] = [{bstack11111_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ⎍"): [bstack11111_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭⎎")]}]
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⎏")] = bstack11lll11l_opy_[bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⎐")]
    return bstack1ll1ll11_opy_
def bstack1lll1ll1l11l_opy_(test, bstack1l111ll1_opy_, bstack1ll1l1l1l_opy_, result, call, outcome, bstack1lll1ll1l1l1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1l111ll1_opy_[bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⎑")]
    hook_name = bstack1l111ll1_opy_[bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ⎒")]
    hook_data = {
        bstack11111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⎓"): bstack1l111ll1_opy_[bstack11111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⎔")],
        bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⎕"): bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ⎖"),
        bstack11111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⎗"): bstack11111_opy_ (u"ࠬࢁࡽࠨ⎘").format(bstack11l111ll11l_opy_(hook_name)),
        bstack11111_opy_ (u"࠭ࡢࡰࡦࡼࠫ⎙"): {
            bstack11111_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬ⎚"): bstack11111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ⎛"),
            bstack11111_opy_ (u"ࠩࡦࡳࡩ࡫ࠧ⎜"): None
        },
        bstack11111_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩ⎝"): test.name,
        bstack11111_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫ⎞"): bstack11llll11_opy_.bstack1ll1l111_opy_(test, hook_name),
        bstack11111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ⎟"): file_path,
        bstack11111_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨ⎠"): file_path,
        bstack11111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⎡"): bstack11111_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⎢"),
        bstack11111_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧ⎣"): file_path,
        bstack11111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⎤"): bstack1l111ll1_opy_[bstack11111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⎥")],
        bstack11111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ⎦"): bstack11111_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨ⎧") if bstack1lll1lllllll_opy_ == bstack11111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫ⎨") else bstack11111_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ⎩"),
        bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬ⎪"): hook_type
    }
    bstack1l1111ll11l_opy_ = bstack1l1111ll_opy_(_1ll1l1ll_opy_.get(test.nodeid, None))
    if bstack1l1111ll11l_opy_:
        hook_data[bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡯ࡤࠨ⎫")] = bstack1l1111ll11l_opy_
    if result:
        hook_data[bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⎬")] = result.outcome
        hook_data[bstack11111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭⎭")] = result.duration * 1000
        hook_data[bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⎮")] = bstack1l111ll1_opy_[bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎯")]
        if result.failed:
            hook_data[bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⎰")] = bstack1l11lll1_opy_.bstack111111lll1_opy_(call.excinfo.typename)
            hook_data[bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ⎱")] = bstack1l11lll1_opy_.bstack1llll1l1lll1_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⎲")] = bstack1111llll1l1_opy_(outcome)
        hook_data[bstack11111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⎳")] = 100
        hook_data[bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⎴")] = bstack1l111ll1_opy_[bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⎵")]
        if hook_data[bstack11111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⎶")] == bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ⎷"):
            hook_data[bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ⎸")] = bstack11111_opy_ (u"࡙ࠪࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠫ⎹")  # bstack1lll1ll1l111_opy_
            hook_data[bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ⎺")] = [{bstack11111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ⎻"): [bstack11111_opy_ (u"࠭ࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠪ⎼")]}]
    if bstack1lll1ll1l1l1_opy_:
        hook_data[bstack11111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⎽")] = bstack1lll1ll1l1l1_opy_.result
        hook_data[bstack11111_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩ⎾")] = bstack111l11l11l1_opy_(bstack1l111ll1_opy_[bstack11111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⎿")], bstack1l111ll1_opy_[bstack11111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⏀")])
        hook_data[bstack11111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏁")] = bstack1l111ll1_opy_[bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏂")]
        if hook_data[bstack11111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⏃")] == bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⏄"):
            hook_data[bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⏅")] = bstack1l11lll1_opy_.bstack111111lll1_opy_(bstack1lll1ll1l1l1_opy_.exception_type)
            hook_data[bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ⏆")] = [{bstack11111_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭⏇"): bstack111ll1111ll_opy_(bstack1lll1ll1l1l1_opy_.exception)}]
    return hook_data
def bstack1lll1lllll1l_opy_(test, bstack11lll11l_opy_, bstack1ll1l1l1l_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack11111_opy_ (u"ࠫࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡴࡦࡵࡷࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠣ࠱ࠥࢁࡽࠨ⏈").format(bstack1ll1l1l1l_opy_))
    bstack1ll1ll11_opy_ = bstack1lll1ll1ll11_opy_(test, bstack11lll11l_opy_, result, call, bstack1ll1l1l1l_opy_, outcome)
    driver = getattr(test, bstack11111_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭⏉"), None)
    if bstack1ll1l1l1l_opy_ == bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⏊") and driver:
        bstack1ll1ll11_opy_[bstack11111_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭⏋")] = bstack1l11lll1_opy_.bstack1l1l1lll_opy_(driver)
    if bstack1ll1l1l1l_opy_ == bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩ⏌"):
        bstack1ll1l1l1l_opy_ = bstack11111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⏍")
    bstack11lll111_opy_ = {
        bstack11111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⏎"): bstack1ll1l1l1l_opy_,
        bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⏏"): bstack1ll1ll11_opy_
    }
    bstack1l11lll1_opy_.bstack1ll11lll_opy_(bstack11lll111_opy_)
    if bstack1ll1l1l1l_opy_ == bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⏐"):
        threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⏑"): bstack11111_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ⏒")}
    elif bstack1ll1l1l1l_opy_ == bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⏓"):
        threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ⏔"): getattr(result, bstack11111_opy_ (u"ࠪࡳࡺࡺࡣࡰ࡯ࡨࠫ⏕"), bstack11111_opy_ (u"ࠫࠬ⏖"))}
def bstack1lll1ll11ll1_opy_(test, bstack11lll11l_opy_, bstack1ll1l1l1l_opy_, result=None, call=None, outcome=None, bstack1lll1ll1l1l1_opy_=None):
    logger.debug(bstack11111_opy_ (u"ࠬࡹࡥ࡯ࡦࡢ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡩࡱࡲ࡯ࠥࡪࡡࡵࡣ࠯ࠤࡪࡼࡥ࡯ࡶࡗࡽࡵ࡫ࠠ࠮ࠢࡾࢁࠬ⏗").format(bstack1ll1l1l1l_opy_))
    hook_data = bstack1lll1ll1l11l_opy_(test, bstack11lll11l_opy_, bstack1ll1l1l1l_opy_, result, call, outcome, bstack1lll1ll1l1l1_opy_)
    bstack11lll111_opy_ = {
        bstack11111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⏘"): bstack1ll1l1l1l_opy_,
        bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩ⏙"): hook_data
    }
    bstack1l11lll1_opy_.bstack1ll11lll_opy_(bstack11lll111_opy_)
def bstack1l1111ll_opy_(bstack11lll11l_opy_):
    if not bstack11lll11l_opy_:
        return None
    if bstack11lll11l_opy_.get(bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ⏚"), None):
        return getattr(bstack11lll11l_opy_[bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ⏛")], bstack11111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⏜"), None)
    return bstack11lll11l_opy_.get(bstack11111_opy_ (u"ࠫࡺࡻࡩࡥࠩ⏝"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.LOG, bstack1lll1l1ll11_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.LOG, bstack1lll1l1ll11_opy_.POST, request, caplog)
        return # skip all existing operations
    try:
        if not bstack1l11lll1_opy_.on():
            return
        places = [bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ⏞"), bstack11111_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ⏟"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ⏠")]
        logs = []
        for bstack1llll111l11l_opy_ in places:
            records = caplog.get_records(bstack1llll111l11l_opy_)
            bstack1lll1ll1l1ll_opy_ = bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⏡") if bstack1llll111l11l_opy_ == bstack11111_opy_ (u"ࠩࡦࡥࡱࡲࠧ⏢") else bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⏣")
            bstack1lll1ll1ll1l_opy_ = request.node.nodeid + (bstack11111_opy_ (u"ࠫࠬ⏤") if bstack1llll111l11l_opy_ == bstack11111_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ⏥") else bstack11111_opy_ (u"࠭࠭ࠨ⏦") + bstack1llll111l11l_opy_)
            test_uuid = bstack1l1111ll_opy_(_1ll1l1ll_opy_.get(bstack1lll1ll1ll1l_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack111l1111l1l_opy_(record.message):
                    continue
                logs.append({
                    bstack11111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⏧"): bstack1111l1ll111_opy_(record.created).isoformat() + bstack11111_opy_ (u"ࠨ࡜ࠪ⏨"),
                    bstack11111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⏩"): record.levelname,
                    bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⏪"): record.message,
                    bstack1lll1ll1l1ll_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1l11lll1_opy_.bstack11llllll_opy_(logs)
    except Exception as err:
        print(bstack11111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡩ࡯࡯ࡦࡢࡪ࡮ࡾࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ⏫"), str(err))
def bstack11ll111ll1_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1l1l1llll1_opy_
    bstack1l1111lll1_opy_ = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ⏬"), None) and bstack1l1lllll_opy_(
            threading.current_thread(), bstack11111_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ⏭"), None)
    bstack1l1l1ll111_opy_ = getattr(driver, bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ⏮"), None) != None and getattr(driver, bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ⏯"), None) == True
    if sequence == bstack11111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ⏰") and driver != None:
      if not bstack1l1l1llll1_opy_ and bstack1lll1ll1lll_opy_() and bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⏱") in CONFIG and CONFIG[bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⏲")] == True and bstack11l1l1l1l1_opy_.bstack1ll11111l1_opy_(driver_command) and (bstack1l1l1ll111_opy_ or bstack1l1111lll1_opy_) and not bstack11l111l1l1_opy_(args):
        try:
          bstack1l1l1llll1_opy_ = True
          logger.debug(bstack11111_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧ⏳").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11111_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫ⏴").format(str(err)))
        bstack1l1l1llll1_opy_ = False
    if sequence == bstack11111_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭⏵"):
        if driver_command == bstack11111_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ⏶"):
            bstack1l11lll1_opy_.bstack1111ll1l1l_opy_({
                bstack11111_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ⏷"): response[bstack11111_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ⏸")],
                bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⏹"): store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ⏺")]
            })
def bstack11l1ll1l11_opy_():
    global bstack1l111ll11_opy_
    bstack111ll1ll1l_opy_.bstack1l111lll11_opy_()
    logging.shutdown()
    bstack1l11lll1_opy_.bstack1l1l1l1l_opy_()
    for driver in bstack1l111ll11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1llll1ll_opy_(*args):
    global bstack1l111ll11_opy_
    bstack1l11lll1_opy_.bstack1l1l1l1l_opy_()
    for driver in bstack1l111ll11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11lllll11l_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l11l11ll_opy_=bstack1l111l11ll_opy_)
def bstack111l11l1l1_opy_(self, *args, **kwargs):
    bstack1111ll1lll_opy_ = bstack1ll1ll111_opy_(self, *args, **kwargs)
    bstack1l11l11l1l_opy_ = getattr(threading.current_thread(), bstack11111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧ⏻"), None)
    if bstack1l11l11l1l_opy_ and bstack1l11l11l1l_opy_.get(bstack11111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⏼"), bstack11111_opy_ (u"ࠨࠩ⏽")) == bstack11111_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪ⏾"):
        bstack1l11lll1_opy_.bstack1l1lll1ll_opy_(self)
    return bstack1111ll1lll_opy_
@measure(event_name=EVENTS.bstack11l1l1ll1_opy_, stage=STAGE.bstack1l1ll111l1_opy_, bstack11l11l11ll_opy_=bstack1l111l11ll_opy_)
def bstack11ll111ll_opy_(framework_name):
    from bstack_utils.config import Config
    bstack11l1111l_opy_ = Config.bstack111111ll_opy_()
    if bstack11l1111l_opy_.get_property(bstack11111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧ⏿")):
        return
    bstack11l1111l_opy_.set_property(bstack11111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨ␀"), True)
    global bstack11111ll1l_opy_
    global bstack1lllll1lll_opy_
    bstack11111ll1l_opy_ = framework_name
    logger.info(bstack1l11ll11l_opy_.format(bstack11111ll1l_opy_.split(bstack11111_opy_ (u"ࠬ࠳ࠧ␁"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1lll1ll1lll_opy_():
            Service.start = bstack1l11ll1l1_opy_
            Service.stop = bstack1l11l1l111_opy_
            webdriver.Remote.get = bstack11ll11l111_opy_
            webdriver.Remote.__init__ = bstack11l111lll1_opy_
            if not isinstance(os.getenv(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡁࡓࡃࡏࡐࡊࡒࠧ␂")), str):
                return
            WebDriver.quit = bstack111llll111_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1l11lll1_opy_.on():
            webdriver.Remote.__init__ = bstack111l11l1l1_opy_
        bstack1lllll1lll_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack11111_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬ␃")):
        bstack1lllll1lll_opy_ = eval(os.environ.get(bstack11111_opy_ (u"ࠨࡕࡈࡐࡊࡔࡉࡖࡏࡢࡓࡗࡥࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡍࡓ࡙ࡔࡂࡎࡏࡉࡉ࠭␄")))
    if not bstack1lllll1lll_opy_:
        bstack111l11l11l_opy_(bstack11111_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ␅"), bstack1ll11ll1ll_opy_)
    if bstack1l1llllll_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack11111_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ␆")) and callable(getattr(RemoteConnection, bstack11111_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ␇"))):
                RemoteConnection._get_proxy_url = bstack111ll1l1l1_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack111ll1l1l1_opy_
        except Exception as e:
            logger.error(bstack1111ll1ll_opy_.format(str(e)))
    if bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ␈") in str(framework_name).lower():
        if not bstack1lll1ll1lll_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1111l11l1_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1111lll111_opy_
            Config.getoption = bstack1111lllll_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1ll11l111_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll11lll1l_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l11l11ll_opy_=bstack1l111l11ll_opy_)
def bstack111llll111_opy_(self):
    global bstack11111ll1l_opy_
    global bstack1lll111l11_opy_
    global bstack11ll1lllll_opy_
    try:
        if bstack11111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭␉") in bstack11111ll1l_opy_ and self.session_id != None and bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫ␊"), bstack11111_opy_ (u"ࠨࠩ␋")) != bstack11111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ␌"):
            bstack11l1lll1l1_opy_ = bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ␍") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ␎")
            bstack1llll111ll_opy_(logger, True)
            if os.environ.get(bstack11111_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ␏"), None):
                self.execute_script(
                    bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ␐") + json.dumps(
                        os.environ.get(bstack11111_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪ␑"))) + bstack11111_opy_ (u"ࠨࡿࢀࠫ␒"))
            if self != None:
                bstack1111ll1l11_opy_(self, bstack11l1lll1l1_opy_, bstack11111_opy_ (u"ࠩ࠯ࠤࠬ␓").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1l1l11111l1_opy_(bstack1l1l111l1l1_opy_):
            item = store.get(bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ␔"), None)
            if item is not None and bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ␕"), None):
                bstack11l111ll_opy_.bstack1lll1llll_opy_(self, bstack1l11111l1_opy_, logger, item)
        threading.current_thread().testStatus = bstack11111_opy_ (u"ࠬ࠭␖")
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢ␗") + str(e))
    bstack11ll1lllll_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack11llll1ll_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l11l11ll_opy_=bstack1l111l11ll_opy_)
def bstack11l111lll1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1lll111l11_opy_
    global bstack1l111l11ll_opy_
    global bstack1l1111111l_opy_
    global bstack11111ll1l_opy_
    global bstack1ll1ll111_opy_
    global bstack1l111ll11_opy_
    global bstack1ll1lllll1_opy_
    global bstack1ll1ll1111_opy_
    global bstack1l11111l1_opy_
    CONFIG[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ␘")] = str(bstack11111ll1l_opy_) + str(__version__)
    command_executor = bstack1ll111111l_opy_(bstack1ll1lllll1_opy_, CONFIG)
    logger.debug(bstack1l11lll11_opy_.format(command_executor))
    proxy = bstack1l1ll1l111_opy_(CONFIG, proxy)
    bstack11l1l1l11l_opy_ = 0
    try:
        if bstack1l1111111l_opy_ is True:
            bstack11l1l1l11l_opy_ = int(os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ␙")))
    except:
        bstack11l1l1l11l_opy_ = 0
    bstack1l11l1l11l_opy_ = bstack111ll11ll_opy_(CONFIG, bstack11l1l1l11l_opy_)
    logger.debug(bstack1lllll1ll1_opy_.format(str(bstack1l11l1l11l_opy_)))
    bstack1l11111l1_opy_ = CONFIG.get(bstack11111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ␚"))[bstack11l1l1l11l_opy_]
    if bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ␛") in CONFIG and CONFIG[bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ␜")]:
        bstack1lll1l1lll_opy_(bstack1l11l1l11l_opy_, bstack1ll1ll1111_opy_)
    if bstack1lll1ll1l_opy_.bstack1l11lll1l1_opy_(CONFIG, bstack11l1l1l11l_opy_) and bstack1lll1ll1l_opy_.bstack111l1l1ll_opy_(bstack1l11l1l11l_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1l1l11111l1_opy_(bstack1l1l111l1l1_opy_):
            bstack1lll1ll1l_opy_.set_capabilities(bstack1l11l1l11l_opy_, CONFIG)
    if desired_capabilities:
        bstack1lllll111l_opy_ = bstack111l1lllll_opy_(desired_capabilities)
        bstack1lllll111l_opy_[bstack11111_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ␝")] = bstack1lll11lll1_opy_(CONFIG)
        bstack1l1ll1llll_opy_ = bstack111ll11ll_opy_(bstack1lllll111l_opy_)
        if bstack1l1ll1llll_opy_:
            bstack1l11l1l11l_opy_ = update(bstack1l1ll1llll_opy_, bstack1l11l1l11l_opy_)
        desired_capabilities = None
    if options:
        bstack1ll111ll1_opy_(options, bstack1l11l1l11l_opy_)
    if not options:
        options = bstack11llll111l_opy_(bstack1l11l1l11l_opy_)
    if proxy and bstack1lll1l11l1_opy_() >= version.parse(bstack11111_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭␞")):
        options.proxy(proxy)
    if options and bstack1lll1l11l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭␟")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1lll1l11l1_opy_() < version.parse(bstack11111_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ␠")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1l11l1l11l_opy_)
    logger.info(bstack1ll1lllll_opy_)
    bstack11l1ll11l_opy_.end(EVENTS.bstack11l1l1ll1_opy_.value, EVENTS.bstack11l1l1ll1_opy_.value + bstack11111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ␡"),
                               EVENTS.bstack11l1l1ll1_opy_.value + bstack11111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ␢"), True, None)
    try:
        if bstack1lll1l11l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ␣")):
            bstack1ll1ll111_opy_(self, command_executor=command_executor,
                      options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
        elif bstack1lll1l11l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ␤")):
            bstack1ll1ll111_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities, options=options,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        elif bstack1lll1l11l1_opy_() >= version.parse(bstack11111_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭␥")):
            bstack1ll1ll111_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        else:
            bstack1ll1ll111_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive)
    except Exception as bstack1l1l1l11ll_opy_:
        logger.error(bstack1ll1ll1l11_opy_.format(bstack11111_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰ࠭␦"), str(bstack1l1l1l11ll_opy_)))
        raise bstack1l1l1l11ll_opy_
    try:
        bstack11l11111l_opy_ = bstack11111_opy_ (u"ࠨࠩ␧")
        if bstack1lll1l11l1_opy_() >= version.parse(bstack11111_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪ␨")):
            bstack11l11111l_opy_ = self.caps.get(bstack11111_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥ␩"))
        else:
            bstack11l11111l_opy_ = self.capabilities.get(bstack11111_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ␪"))
        if bstack11l11111l_opy_:
            bstack1l1llll11_opy_(bstack11l11111l_opy_)
            if bstack1lll1l11l1_opy_() <= version.parse(bstack11111_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ␫")):
                self.command_executor._url = bstack11111_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ␬") + bstack1ll1lllll1_opy_ + bstack11111_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦ␭")
            else:
                self.command_executor._url = bstack11111_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ␮") + bstack11l11111l_opy_ + bstack11111_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥ␯")
            logger.debug(bstack11l11llll_opy_.format(bstack11l11111l_opy_))
        else:
            logger.debug(bstack11l1lll11l_opy_.format(bstack11111_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦ␰")))
    except Exception as e:
        logger.debug(bstack11l1lll11l_opy_.format(e))
    bstack1lll111l11_opy_ = self.session_id
    if bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ␱") in bstack11111ll1l_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ␲"), None)
        if item:
            bstack1lll1lll1l1l_opy_ = getattr(item, bstack11111_opy_ (u"࠭࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࡢࡷࡹࡧࡲࡵࡧࡧࠫ␳"), False)
            if not getattr(item, bstack11111_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ␴"), None) and bstack1lll1lll1l1l_opy_:
                setattr(store[bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ␵")], bstack11111_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ␶"), self)
        bstack1l11l11l1l_opy_ = getattr(threading.current_thread(), bstack11111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫ␷"), None)
        if bstack1l11l11l1l_opy_ and bstack1l11l11l1l_opy_.get(bstack11111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ␸"), bstack11111_opy_ (u"ࠬ࠭␹")) == bstack11111_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ␺"):
            bstack1l11lll1_opy_.bstack1l1lll1ll_opy_(self)
    bstack1l111ll11_opy_.append(self)
    if bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ␻") in CONFIG and bstack11111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭␼") in CONFIG[bstack11111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ␽")][bstack11l1l1l11l_opy_]:
        bstack1l111l11ll_opy_ = CONFIG[bstack11111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭␾")][bstack11l1l1l11l_opy_][bstack11111_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ␿")]
    logger.debug(bstack1llll1l1ll_opy_.format(bstack1lll111l11_opy_))
@measure(event_name=EVENTS.bstack111l111111_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l11l11ll_opy_=bstack1l111l11ll_opy_)
def bstack11ll11l111_opy_(self, url):
    global bstack1l1l1l111l_opy_
    global CONFIG
    try:
        bstack1ll11l1l1l_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1ll1ll1ll1_opy_.format(str(err)))
    try:
        bstack1l1l1l111l_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack1lll11ll11_opy_):
                bstack1ll11l1l1l_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1ll1ll1ll1_opy_.format(str(err)))
        raise e
def bstack1ll1l1ll1_opy_(item, when):
    global bstack111lll11l1_opy_
    try:
        bstack111lll11l1_opy_(item, when)
    except Exception as e:
        pass
def bstack1ll11l111_opy_(item, call, rep):
    global bstack1lll111ll1_opy_
    global bstack1l111ll11_opy_
    name = bstack11111_opy_ (u"ࠬ࠭⑀")
    try:
        if rep.when == bstack11111_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ⑁"):
            bstack1lll111l11_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack11111_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⑂"))
            try:
                if (str(skipSessionName).lower() != bstack11111_opy_ (u"ࠨࡶࡵࡹࡪ࠭⑃")):
                    name = str(rep.nodeid)
                    bstack1ll11l1l11_opy_ = bstack1lllll1l1l_opy_(bstack11111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⑄"), name, bstack11111_opy_ (u"ࠪࠫ⑅"), bstack11111_opy_ (u"ࠫࠬ⑆"), bstack11111_opy_ (u"ࠬ࠭⑇"), bstack11111_opy_ (u"࠭ࠧ⑈"))
                    os.environ[bstack11111_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪ⑉")] = name
                    for driver in bstack1l111ll11_opy_:
                        if bstack1lll111l11_opy_ == driver.session_id:
                            driver.execute_script(bstack1ll11l1l11_opy_)
            except Exception as e:
                logger.debug(bstack11111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ⑊").format(str(e)))
            try:
                bstack11l11l1l1_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ⑋"):
                    status = bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⑌") if rep.outcome.lower() == bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⑍") else bstack11111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ⑎")
                    reason = bstack11111_opy_ (u"࠭ࠧ⑏")
                    if status == bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⑐"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11111_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭⑑") if status == bstack11111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⑒") else bstack11111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ⑓")
                    data = name + bstack11111_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭⑔") if status == bstack11111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ⑕") else name + bstack11111_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠡࠡࠩ⑖") + reason
                    bstack11l1ll1l1_opy_ = bstack1lllll1l1l_opy_(bstack11111_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ⑗"), bstack11111_opy_ (u"ࠨࠩ⑘"), bstack11111_opy_ (u"ࠩࠪ⑙"), bstack11111_opy_ (u"ࠪࠫ⑚"), level, data)
                    for driver in bstack1l111ll11_opy_:
                        if bstack1lll111l11_opy_ == driver.session_id:
                            driver.execute_script(bstack11l1ll1l1_opy_)
            except Exception as e:
                logger.debug(bstack11111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡥࡲࡲࡹ࡫ࡸࡵࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ⑛").format(str(e)))
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡵࡷࡥࡹ࡫ࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻࡾࠩ⑜").format(str(e)))
    bstack1lll111ll1_opy_(item, call, rep)
notset = Notset()
def bstack1111lllll_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack111lll1ll1_opy_
    if str(name).lower() == bstack11111_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭⑝"):
        return bstack11111_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨ⑞")
    else:
        return bstack111lll1ll1_opy_(self, name, default, skip)
def bstack111ll1l1l1_opy_(self):
    global CONFIG
    global bstack1l1l1ll11_opy_
    try:
        proxy = bstack1lll11111l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11111_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭⑟")):
                proxies = bstack11ll11l1ll_opy_(proxy, bstack1ll111111l_opy_())
                if len(proxies) > 0:
                    protocol, bstack111l1ll11l_opy_ = proxies.popitem()
                    if bstack11111_opy_ (u"ࠤ࠽࠳࠴ࠨ①") in bstack111l1ll11l_opy_:
                        return bstack111l1ll11l_opy_
                    else:
                        return bstack11111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ②") + bstack111l1ll11l_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣ③").format(str(e)))
    return bstack1l1l1ll11_opy_(self)
def bstack1l1llllll_opy_():
    return (bstack11111_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ④") in CONFIG or bstack11111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ⑤") in CONFIG) and bstack11ll1lll11_opy_() and bstack1lll1l11l1_opy_() >= version.parse(
        bstack1llllll1ll_opy_)
def bstack11l11lll1_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l111l11ll_opy_
    global bstack1l1111111l_opy_
    global bstack11111ll1l_opy_
    CONFIG[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ⑥")] = str(bstack11111ll1l_opy_) + str(__version__)
    bstack11l1l1l11l_opy_ = 0
    try:
        if bstack1l1111111l_opy_ is True:
            bstack11l1l1l11l_opy_ = int(os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ⑦")))
    except:
        bstack11l1l1l11l_opy_ = 0
    CONFIG[bstack11111_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ⑧")] = True
    bstack1l11l1l11l_opy_ = bstack111ll11ll_opy_(CONFIG, bstack11l1l1l11l_opy_)
    logger.debug(bstack1lllll1ll1_opy_.format(str(bstack1l11l1l11l_opy_)))
    if CONFIG.get(bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ⑨")):
        bstack1lll1l1lll_opy_(bstack1l11l1l11l_opy_, bstack1ll1ll1111_opy_)
    if bstack11111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ⑩") in CONFIG and bstack11111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⑪") in CONFIG[bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⑫")][bstack11l1l1l11l_opy_]:
        bstack1l111l11ll_opy_ = CONFIG[bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⑬")][bstack11l1l1l11l_opy_][bstack11111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⑭")]
    import urllib
    import json
    if bstack11111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⑮") in CONFIG and str(CONFIG[bstack11111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ⑯")]).lower() != bstack11111_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ⑰"):
        bstack1l1l11ll1l_opy_ = bstack1l111111ll_opy_()
        bstack1l1lll11l1_opy_ = bstack1l1l11ll1l_opy_ + urllib.parse.quote(json.dumps(bstack1l11l1l11l_opy_))
    else:
        bstack1l1lll11l1_opy_ = bstack11111_opy_ (u"ࠬࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠧ⑱") + urllib.parse.quote(json.dumps(bstack1l11l1l11l_opy_))
    browser = self.connect(bstack1l1lll11l1_opy_)
    return browser
def bstack1lllll11l1_opy_():
    global bstack1lllll1lll_opy_
    global bstack11111ll1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111llll1_opy_
        if not bstack1lll1ll1lll_opy_():
            global bstack111l111ll1_opy_
            if not bstack111l111ll1_opy_:
                from bstack_utils.helper import bstack11l111llll_opy_, bstack11l1l11l1l_opy_
                bstack111l111ll1_opy_ = bstack11l111llll_opy_()
                bstack11l1l11l1l_opy_(bstack11111ll1l_opy_)
            BrowserType.connect = bstack1111llll1_opy_
            return
        BrowserType.launch = bstack11l11lll1_opy_
        bstack1lllll1lll_opy_ = True
    except Exception as e:
        pass
def bstack1llll1111l1l_opy_():
    global CONFIG
    global bstack1lll1l1111_opy_
    global bstack1ll1lllll1_opy_
    global bstack1ll1ll1111_opy_
    global bstack1l1111111l_opy_
    global bstack111lll111_opy_
    CONFIG = json.loads(os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠬ⑲")))
    bstack1lll1l1111_opy_ = eval(os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ⑳")))
    bstack1ll1lllll1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡉࡗࡅࡣ࡚ࡘࡌࠨ⑴"))
    bstack1l1lll1l11_opy_(CONFIG, bstack1lll1l1111_opy_)
    bstack111lll111_opy_ = bstack111ll1ll1l_opy_.configure_logger(CONFIG, bstack111lll111_opy_)
    if cli.bstack1ll1ll11l_opy_():
        bstack11llll1lll_opy_.invoke(Events.CONNECT, bstack1111lll11_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ⑵"), bstack11111_opy_ (u"ࠪ࠴ࠬ⑶")))
        cli.bstack1l1l1l1111l_opy_(cli_context.platform_index)
        cli.bstack1l1l1111ll1_opy_(bstack1ll111111l_opy_(bstack1ll1lllll1_opy_, CONFIG), cli_context.platform_index, bstack11llll111l_opy_)
        cli.bstack1l1l11l1111_opy_()
        logger.debug(bstack11111_opy_ (u"ࠦࡈࡒࡉࠡ࡫ࡶࠤࡦࡩࡴࡪࡸࡨࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࠥ⑷") + str(cli_context.platform_index) + bstack11111_opy_ (u"ࠧࠨ⑸"))
        return # skip all existing operations
    global bstack1ll1ll111_opy_
    global bstack11ll1lllll_opy_
    global bstack1lll11l1l1_opy_
    global bstack1ll1l111l1_opy_
    global bstack1lll1ll11l_opy_
    global bstack11111ll11_opy_
    global bstack1ll1ll1l1_opy_
    global bstack1l1l1l111l_opy_
    global bstack1l1l1ll11_opy_
    global bstack111lll1ll1_opy_
    global bstack111lll11l1_opy_
    global bstack1lll111ll1_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1ll1ll111_opy_ = webdriver.Remote.__init__
        bstack11ll1lllll_opy_ = WebDriver.quit
        bstack1ll1ll1l1_opy_ = WebDriver.close
        bstack1l1l1l111l_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11111_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ⑹") in CONFIG or bstack11111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ⑺") in CONFIG) and bstack11ll1lll11_opy_():
        if bstack1lll1l11l1_opy_() < version.parse(bstack1llllll1ll_opy_):
            logger.error(bstack11l111l1ll_opy_.format(bstack1lll1l11l1_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack11111_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ⑻")) and callable(getattr(RemoteConnection, bstack11111_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ⑼"))):
                    bstack1l1l1ll11_opy_ = RemoteConnection._get_proxy_url
                else:
                    from selenium.webdriver.remote.client_config import ClientConfig
                    bstack1l1l1ll11_opy_ = ClientConfig.get_proxy_url
            except Exception as e:
                logger.error(bstack1111ll1ll_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack111lll1ll1_opy_ = Config.getoption
        from _pytest import runner
        bstack111lll11l1_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack11l11l1l_opy_)
    try:
        from pytest_bdd import reporting
        bstack1lll111ll1_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫ⑽"))
    bstack1ll1ll1111_opy_ = CONFIG.get(bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ⑾"), {}).get(bstack11111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ⑿"))
    bstack1l1111111l_opy_ = True
    bstack11ll111ll_opy_(bstack1lll11ll1l_opy_)
if (bstack111l11lllll_opy_()):
    bstack1llll1111l1l_opy_()
@error_handler(class_method=False)
def bstack1lll1lll1111_opy_(hook_name, event, bstack1ll1l11llll_opy_=None):
    if hook_name not in [bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧ⒀"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫ⒁"), bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧ⒂"), bstack11111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫ⒃"), bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ⒄"), bstack11111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬ⒅"), bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫ⒆"), bstack11111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨ⒇")]:
        return
    node = store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⒈")]
    if hook_name in [bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧ⒉"), bstack11111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫ⒊")]:
        node = store[bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡲࡵࡤࡶ࡮ࡨࡣ࡮ࡺࡥ࡮ࠩ⒋")]
    elif hook_name in [bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩ⒌"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭⒍")]:
        node = store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡤ࡮ࡤࡷࡸࡥࡩࡵࡧࡰࠫ⒎")]
    hook_type = bstack11l11l11l11_opy_(hook_name)
    if event == bstack11111_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧ⒏"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_[hook_type], bstack1lll1l1ll11_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack1l111ll1_opy_ = {
            bstack11111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⒐"): uuid,
            bstack11111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⒑"): bstack1l11llll_opy_(),
            bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨ⒒"): bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩ⒓"),
            bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⒔"): hook_type,
            bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ⒕"): hook_name
        }
        store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⒖")].append(uuid)
        bstack1llll11111ll_opy_ = node.nodeid
        if hook_type == bstack11111_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭⒗"):
            if not _1ll1l1ll_opy_.get(bstack1llll11111ll_opy_, None):
                _1ll1l1ll_opy_[bstack1llll11111ll_opy_] = {bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⒘"): []}
            _1ll1l1ll_opy_[bstack1llll11111ll_opy_][bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⒙")].append(bstack1l111ll1_opy_[bstack11111_opy_ (u"ࠫࡺࡻࡩࡥࠩ⒚")])
        _1ll1l1ll_opy_[bstack1llll11111ll_opy_ + bstack11111_opy_ (u"ࠬ࠳ࠧ⒛") + hook_name] = bstack1l111ll1_opy_
        bstack1lll1ll11ll1_opy_(node, bstack1l111ll1_opy_, bstack11111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⒜"))
    elif event == bstack11111_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭⒝"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_[hook_type], bstack1lll1l1ll11_opy_.POST, node, None, bstack1ll1l11llll_opy_)
            return
        bstack1l1ll1l1_opy_ = node.nodeid + bstack11111_opy_ (u"ࠨ࠯ࠪ⒞") + hook_name
        _1ll1l1ll_opy_[bstack1l1ll1l1_opy_][bstack11111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⒟")] = bstack1l11llll_opy_()
        bstack1lll1lll11l1_opy_(_1ll1l1ll_opy_[bstack1l1ll1l1_opy_][bstack11111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⒠")])
        bstack1lll1ll11ll1_opy_(node, _1ll1l1ll_opy_[bstack1l1ll1l1_opy_], bstack11111_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭⒡"), bstack1lll1ll1l1l1_opy_=bstack1ll1l11llll_opy_)
def bstack1lll1lll1ll1_opy_():
    global bstack1lll1lllllll_opy_
    if bstack11l11l11l1_opy_():
        bstack1lll1lllllll_opy_ = bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩ⒢")
    else:
        bstack1lll1lllllll_opy_ = bstack11111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭⒣")
def pytest_collection_modifyitems(session, config, items):
    bstack11111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡇ࡫࡯ࡸࡪࡸࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࡵࡿࡴࡦࡵࡷࠤ࡮ࡺࡥ࡮ࡵࠣࡦࡦࡹࡥࡥࠢࡲࡲࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤࡸ࡫࡬ࡦࡥࡷࡳࡷࡹࠠࡧࡴࡲࡱࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡳࡸࡨࡶ࠳ࠐࠠࠡࠢࠣࠦࠧࠨ⒤")
    import os
    bstack1llll11111l1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡐࡔࡆࡌࡊ࡙ࡔࡓࡃࡗࡉࡉࡥࡓࡆࡎࡈࡇ࡙ࡕࡒࡔࠩ⒥"))
    if not bstack1llll11111l1_opy_:
        return
    try:
        bstack1lll1lllll11_opy_ = json.loads(bstack1llll11111l1_opy_)
        if not isinstance(bstack1lll1lllll11_opy_, (list, set)) or not bstack1lll1lllll11_opy_:
            return
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠤࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥࡶࡡࡳࡵࡨࠤࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡓࡗࡉࡈࡆࡕࡗࡖࡆ࡚ࡅࡅࡡࡖࡉࡑࡋࡃࡕࡑࡕࡗ࠿ࠦࠢ⒦") + str(e) + bstack11111_opy_ (u"ࠥࠦ⒧"))
        return
    selected = []
    deselected = []
    bstack1lll1llll11l_opy_ = set()
    for selector in bstack1lll1lllll11_opy_:
        if not selector or not isinstance(selector, str):
            continue
        bstack1lll1llll11l_opy_.add(selector)
    for item in items:
        nodeid = getattr(item, bstack11111_opy_ (u"ࠫࡳࡵࡤࡦ࡫ࡧࠫ⒨"), None)
        if not nodeid:
            deselected.append(item)
            continue
        if (
            nodeid in bstack1lll1llll11l_opy_ or
            any(sel in nodeid for sel in bstack1lll1llll11l_opy_)
        ):
            selected.append(item)
        else:
            deselected.append(item)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected
def pytest_collection_finish(session):
    bstack11111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡉࡡ࡭࡮ࡨࡨࠥࡧࡦࡵࡧࡵࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡ࡫ࡩࠤ࠲࠳ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭࡯ࡱࡧࡩ࡮ࡪࡳࠡࡨ࡯ࡥ࡬ࠦࡩࡴࠢࡸࡷࡪࡪ࠮ࠋࠢࠣࠤࠥࡖࡲࡪࡰࡷࡷࠥࡴ࡯ࡥࡧ࡬ࡨࡸࠦࡣ࡭ࡧࡤࡲࡱࡿࠠࡢࡰࡧࠤࡪࡾࡩࡵࡵࠣࡴࡾࡺࡥࡴࡶࠣ࡭ࡳࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰ࠰ࡳࡳࡲࡹࠡ࡯ࡲࡨࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢ⒩")
    try:
        bstack1llll1111ll1_opy_ = session.config.getoption(bstack11111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡣࡰ࡮࡯ࡩࡨࡺ࡟࡯ࡱࡧࡩ࡮ࡪࡳࠨ⒪"), False)
        if not bstack1llll1111ll1_opy_:
            return
        bstack1lll1llll1l1_opy_ = session.items
        bstack1lll1lll11ll_opy_ = [item.nodeid for item in bstack1lll1llll1l1_opy_]
        if bstack1lll1lll11ll_opy_:
            print(bstack11111_opy_ (u"ࠢ࡝ࡰࠥ⒫").join(bstack1lll1lll11ll_opy_))
            print(bstack1lll1ll11ll_opy_ (u"ࠣ࡞ࡱࡿࡱ࡫࡮ࠩࡰࡲࡨࡪ࡯ࡤࡴࠫࢀࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠨ⒬"))
        else:
            print(bstack11111_opy_ (u"ࠤࡑࡳࠥࡺࡥࡴࡶࡶࠤࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠢ⒭"))
        session.config.option.bstack1llll111111l_opy_ = True
    except Exception as e:
        logger.error(bstack11111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡨࡳࡵࡣࡦ࡯ࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࠼ࠣࠦ⒮") + str(e) + bstack11111_opy_ (u"ࠦࠧ⒯"))
def bstack1llllllll_opy_(bstack111l11l1_opy_=None, bstack11l1l111_opy_=None, bstack1llll111l_opy_=False):
    bstack11111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡖࡲࡰࡩࡵࡥࡲࡳࡡࡵ࡫ࡦࡥࡱࡲࡹࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡶࡹࡧࡶࡲࡰࡥࡨࡷࡸ࠴ࠊࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡹ࡫ࡳࡵࡡࡤࡶ࡬ࡹࠠࠩ࡮࡬ࡷࡹ࠲ࠠࡰࡲࡷ࡭ࡴࡴࡡ࡭ࠫ࠽ࠤࡈࡵ࡭ࡱ࡮ࡨࡸࡪࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡻࡷࡩࡸࡺࠠࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠣ࡭ࡳࡩ࡬ࡶࡦ࡬ࡲ࡬ࠦࡰࡢࡶ࡫ࡷࠥࡧ࡮ࡥࠢࡩࡰࡦ࡭ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡗࡥࡰ࡫ࡳࠡࡲࡵࡩࡨ࡫ࡤࡦࡰࡦࡩࠥࡵࡶࡦࡴࠣࡸࡪࡹࡴࡠࡲࡤࡸ࡭ࡹࠠࡪࡨࠣࡦࡴࡺࡨࠡࡣࡵࡩࠥࡶࡲࡰࡸ࡬ࡨࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡷࡩࡸࡺ࡟ࡱࡣࡷ࡬ࡸࠦࠨ࡭࡫ࡶࡸࠥࡵࡲࠡࡵࡷࡶ࠱ࠦ࡯ࡱࡶ࡬ࡳࡳࡧ࡬ࠪ࠼ࠣࡘࡪࡹࡴࠡࡨ࡬ࡰࡪ࠮ࡳࠪ࠱ࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠭࡯ࡥࡴࠫࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡧࡴࡲࡱ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡄࡣࡱࠤࡧ࡫ࠠࡢࠢࡶ࡭ࡳ࡭࡬ࡦࠢࡳࡥࡹ࡮ࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡰࡴࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡵࡧࡴࡩࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡏࡧ࡯ࡱࡵࡩࡩࠦࡩࡧࠢࡷࡩࡸࡺ࡟ࡢࡴࡪࡷࠥ࡯ࡳࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡹࡩ࡭ࡧࡱࡸࠥ࠮ࡢࡰࡱ࡯࠰ࠥࡵࡰࡵ࡫ࡲࡲࡦࡲࠩ࠻ࠢࡌࡪ࡚ࠥࡲࡶࡧ࠯ࠤࡸࡻࡰࡱࡴࡨࡷࡸ࡫ࡳࠡࡲࡵ࡭ࡳࡺࠠࡰࡷࡷࡴࡺࡺ࠮ࠡࡆࡨࡪࡦࡻ࡬ࡵࠢࡉࡥࡱࡹࡥ࠯ࠌࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡅࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡷࡪࡶ࡫ࠤࡳࡵࡤࡦ࡫ࡧࡷ࠱ࠦࡣࡰࡷࡱࡸ࠱ࠦࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࠍࠤࠥࠦࠠࡆࡺࡤࡱࡵࡲࡥࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡃࠠࡤࡱ࡯ࡰࡪࡩࡴࡠࡶࡨࡷࡹࡹ࡟ࡱࡴࡲ࡫ࡷࡧ࡭࡮ࡣࡷ࡭ࡨࡧ࡬࡭ࡻࠫࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡩࡸࡺ࡟ࡢࡴࡪࡷࡂࡡࠢࡵࡧࡶࡸࡸ࠵ࠢ࠭ࠢࠥ࠱ࡵࠨࠬࠡࠤࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠢ࠭ࠢࠥ࠱࠲ࡪࡲࡪࡸࡨࡶࠧ࠲ࠠࠣࡥ࡫ࡶࡴࡳࡥࠣ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡶࡹࡱࡺࡳࠡ࠿ࠣࡧࡴࡲ࡬ࡦࡥࡷࡣࡹ࡫ࡳࡵࡵࡢࡴࡷࡵࡧࡳࡣࡰࡱࡦࡺࡩࡤࡣ࡯ࡰࡾ࠮ࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࡀ࡟࡙ࠧࡄࡌ࠱ࠥ࠰ࠥࠨࡴࡦࡵࡷࡷ࠴࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰ࠲ࠦࡢ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡷࡺࡲࡴࡴࠢࡀࠤࡨࡵ࡬࡭ࡧࡦࡸࡤࡺࡥࡴࡶࡶࡣࡵࡸ࡯ࡨࡴࡤࡱࡲࡧࡴࡪࡥࡤࡰࡱࡿࠨࡵࡧࡶࡸࡤࡶࡡࡵࡪࡶࡁ࡙ࠧࡄࡌ࠱ࠥ࠭ࠏࠦࠠࠡࠢࠥࠦࠧ⒰")
    try:
        import pytest
        if bstack111l11l1_opy_ is not None:
            args = bstack111l11l1_opy_
        elif bstack11l1l111_opy_ is not None:
            if isinstance(bstack11l1l111_opy_, str):
                args = [bstack11l1l111_opy_]
            elif isinstance(bstack11l1l111_opy_, list):
                args = bstack11l1l111_opy_
            else:
                args = [bstack11111_opy_ (u"ࠨ࠮ࠣ⒱")]
        else:
            args = [bstack11111_opy_ (u"ࠢ࠯ࠤ⒲")]
        bstack1lll1llll111_opy_ = list(args) + [bstack11111_opy_ (u"ࠣ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺࠤ⒳")]
        if bstack1llll111l_opy_:
            bstack1lll1llll111_opy_.extend([
                bstack11111_opy_ (u"ࠤ࠰࠱ࡶࡻࡩࡦࡶࠥ⒴"),
                bstack11111_opy_ (u"ࠥ࠱࠲ࡺࡢ࠾ࡰࡲࠦ⒵"),
                bstack11111_opy_ (u"ࠦ࠲ࡶࠢⒶ"), bstack11111_opy_ (u"ࠧࡴ࡯࠻ࡹࡤࡶࡳ࡯࡮ࡨࡵࠥⒷ"),
                bstack11111_opy_ (u"ࠨ࠭࠮ࡰࡲ࠱ࡸࡻ࡭࡮ࡣࡵࡽࠧⒸ")
            ])
        class bstack1lll1ll11lll_opy_:
            def __init__(self):
                self.collected = []
            def pytest_collection_finish(self, session):
                self.collected = [item.nodeid for item in session.items]
        bstack1lll1ll1lll1_opy_ = bstack1lll1ll11lll_opy_()
        if bstack1llll111l_opy_:
            import sys
            import io
            bstack1lll1ll111l1_opy_ = sys.stdout
            bstack1llll1111l11_opy_ = sys.stderr
            sys.stdout = io.StringIO()
            sys.stderr = io.StringIO()
            try:
                pytest.main(bstack1lll1llll111_opy_ + [bstack11111_opy_ (u"ࠢ࠮ࡲࠥⒹ"), bstack11111_opy_ (u"ࠣࡰࡲ࠾ࡨࡧࡣࡩࡧࡳࡶࡴࡼࡩࡥࡧࡵࠦⒺ")], plugins=[bstack1lll1ll1lll1_opy_])
            finally:
                sys.stdout = bstack1lll1ll111l1_opy_
                sys.stderr = bstack1llll1111l11_opy_
        else:
            pytest.main(bstack1lll1llll111_opy_ + [bstack11111_opy_ (u"ࠤ࠰ࡴࠧⒻ"), bstack11111_opy_ (u"ࠥࡲࡴࡀࡣࡢࡥ࡫ࡩࡵࡸ࡯ࡷ࡫ࡧࡩࡷࠨⒼ")], plugins=[bstack1lll1ll1lll1_opy_])
        bstack1lll1lll11ll_opy_ = bstack1lll1ll1lll1_opy_.collected
        test_files = set()
        for nodeid in bstack1lll1lll11ll_opy_:
            if bstack11111_opy_ (u"ࠦ࠿ࡀࠢⒽ") in nodeid:
                file_path = nodeid.split(bstack11111_opy_ (u"ࠧࡀ࠺ࠣⒾ"), 1)[0]
                if file_path.endswith(bstack11111_opy_ (u"࠭࠮ࡱࡻࠪⒿ")):
                    test_files.add(file_path)
        result = {
            bstack11111_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳࠣⓀ"): True,
            bstack11111_opy_ (u"ࠣࡥࡲࡹࡳࡺࠢⓁ"): len(bstack1lll1lll11ll_opy_),
            bstack11111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࡵࠥⓂ"): bstack1lll1lll11ll_opy_,
            bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹࠢⓃ"): sorted(test_files)
        }
        if not bstack1llll111l_opy_:
            logger.debug(bstack11111_opy_ (u"ࠦࡠࡉ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࡟ࠣࡊࡴࡻ࡮ࡥࠢࡾࡶࡪࡹࡵ࡭ࡶ࡞ࠫࡨࡵࡵ࡯ࡶࠪࡡࢂࠦࡴࡦࡵࡷࡷࠥ࡯࡮ࠡࠤⓄ") + str(len(result[bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴࠩⓅ")])) + bstack11111_opy_ (u"ࠨࠠࡧ࡫࡯ࡩࡸࠨⓆ"))
        return result
    except Exception as e:
        logger.error(bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡶࡴ࡭ࡲࡢ࡯ࡰࡥࡹ࡯ࡣࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲ࠿ࠦࠢⓇ") + str(e) + bstack11111_opy_ (u"ࠣࠤⓈ"))
        return {
            bstack11111_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵࠥⓉ"): False,
            bstack11111_opy_ (u"ࠥࡧࡴࡻ࡮ࡵࠤⓊ"): 0,
            bstack11111_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࡷࠧⓋ"): [],
            bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴࠤⓌ"): []
        }
@bstack1l11lll1_opy_.bstack1llll1l1l111_opy_
def bstack1llll1111111_opy_():
    bstack1lll1lll1ll1_opy_()
    if cli.is_running():
        try:
            bstack11l1ll111ll_opy_(bstack1lll1lll1111_opy_)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡶࠤࡵࡧࡴࡤࡪ࠽ࠤࢀࢃࠢⓍ").format(e))
        return
    if bstack11ll1lll11_opy_():
        bstack11l1111l_opy_ = Config.bstack111111ll_opy_()
        bstack11111_opy_ (u"ࠧࠨࠩࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡈࡲࡶࠥࡶࡰࡱࠢࡀࠤ࠶࠲ࠠ࡮ࡱࡧࡣࡪࡾࡥࡤࡷࡷࡩࠥ࡭ࡥࡵࡵࠣࡹࡸ࡫ࡤࠡࡨࡲࡶࠥࡧ࠱࠲ࡻࠣࡧࡴࡳ࡭ࡢࡰࡧࡷ࠲ࡽࡲࡢࡲࡳ࡭ࡳ࡭ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡌ࡯ࡳࠢࡳࡴࡵࠦ࠾ࠡ࠳࠯ࠤࡲࡵࡤࡠࡧࡻࡩࡨࡻࡴࡦࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡤࡨࡧࡦࡻࡳࡦࠢ࡬ࡸࠥ࡯ࡳࠡࡲࡤࡸࡨ࡮ࡥࡥࠢ࡬ࡲࠥࡧࠠࡥ࡫ࡩࡪࡪࡸࡥ࡯ࡶࠣࡴࡷࡵࡣࡦࡵࡶࠤ࡮ࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡶࡵࠣࡻࡪࠦ࡮ࡦࡧࡧࠤࡹࡵࠠࡶࡵࡨࠤࡘ࡫࡬ࡦࡰ࡬ࡹࡲࡖࡡࡵࡥ࡫ࠬࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡨࡢࡰࡧࡰࡪࡸࠩࠡࡨࡲࡶࠥࡶࡰࡱࠢࡁࠤ࠶ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨࠩࠪⓎ")
        if bstack11l1111l_opy_.get_property(bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬⓏ")):
            if CONFIG.get(bstack11111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩⓐ")) is not None and int(CONFIG[bstack11111_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪⓑ")]) > 1:
                bstack1l111l1ll1_opy_(bstack11ll111ll1_opy_)
            return
        bstack1l111l1ll1_opy_(bstack11ll111ll1_opy_)
    try:
        bstack11l1ll111ll_opy_(bstack1lll1lll1111_opy_)
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡴࠢࡳࡥࡹࡩࡨ࠻ࠢࡾࢁࠧⓒ").format(e))
bstack1llll1111111_opy_()