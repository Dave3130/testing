# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack1l11l1l11_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1l11ll1l1l_opy_, bstack1l111ll111_opy_, update, bstack1l1l1lll11_opy_,
                                       bstack11l1ll1111_opy_, bstack11ll111l1_opy_, bstack11ll111l11_opy_, bstack1lllll111l_opy_,
                                       bstack1ll1l11l1l_opy_, bstack1l11l1l1ll_opy_, bstack1ll111l11l_opy_,
                                       bstack1l1lllll1_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1l11l1111l_opy_)
from browserstack_sdk.bstack111ll11l_opy_ import bstack111l1lll_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1l11l1lll_opy_
from bstack_utils.capture import bstack1l1ll1ll_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack111l111ll1_opy_, bstack1ll11ll1l1_opy_, bstack11111ll11_opy_, \
    bstack1lll1l1ll1_opy_
from bstack_utils.helper import bstack1l11l1ll_opy_, bstack1111ll111ll_opy_, bstack1l1ll111_opy_, bstack1ll11l11l1_opy_, bstack1lll1l1111l_opy_, bstack1lllll11_opy_, \
    bstack1111lll1lll_opy_, \
    bstack1111ll1ll11_opy_, bstack1l11ll1lll_opy_, bstack1lll11llll_opy_, bstack111l1l111l1_opy_, bstack111ll1llll_opy_, Notset, \
    bstack1ll1l111l1_opy_, bstack111l1ll1ll1_opy_, bstack111l1l11ll1_opy_, Result, bstack1111lllll1l_opy_, bstack1111l11ll11_opy_, error_handler, \
    bstack1l1111l111_opy_, bstack111l11ll1_opy_, bstack11l1llll1_opy_, bstack1111llll11l_opy_
from bstack_utils.bstack11l1l1lll11_opy_ import bstack11l1l1llll1_opy_
from bstack_utils.messages import bstack1111l11lll_opy_, bstack11ll1111ll_opy_, bstack11l1l11l1l_opy_, bstack11l1llll1l_opy_, bstack1lll1ll1l_opy_, \
    bstack1ll1l1ll11_opy_, bstack1l111lll1l_opy_, bstack11l1llllll_opy_, bstack111l11l1ll_opy_, bstack1l1ll1111l_opy_, \
    bstack111l1l11l_opy_, bstack11l11111l_opy_, bstack1111l11l11_opy_
from bstack_utils.proxy import bstack111ll11ll_opy_, bstack1l11l1ll1_opy_
from bstack_utils.bstack1l11111lll_opy_ import bstack11l111ll1l1_opy_, bstack11l111ll111_opy_, bstack11l111l1l11_opy_, bstack11l111l1lll_opy_, \
    bstack11l111l11l1_opy_, bstack11l111l1ll1_opy_, bstack11l111l1l1l_opy_, bstack1llll11l1l_opy_, bstack11l111ll1ll_opy_
from bstack_utils.bstack1l1l1ll1l_opy_ import bstack1ll1ll1l1l_opy_
from bstack_utils.bstack1lll111l11_opy_ import bstack1ll1l1l1ll_opy_, bstack1l1l1lll1l_opy_, bstack1ll1l11ll_opy_, \
    bstack11ll1111l1_opy_, bstack1lll11lll1_opy_
from bstack_utils.bstack1l1l11ll_opy_ import bstack1l1l1ll1_opy_
from bstack_utils.bstack1llll111_opy_ import bstack1lll1111_opy_
import bstack_utils.accessibility as bstack1lll11ll1_opy_
from bstack_utils.bstack1l1llll1_opy_ import bstack1l1l1111_opy_
from bstack_utils.bstack111ll11l11_opy_ import bstack111ll11l11_opy_
from bstack_utils.bstack1lll1llll_opy_ import bstack1llll1lll_opy_
from browserstack_sdk.__init__ import bstack1111l1lll1_opy_
from browserstack_sdk.sdk_cli.bstack1l11lllll11_opy_ import bstack1l1l111ll1l_opy_
from browserstack_sdk.sdk_cli.bstack111l1111l1_opy_ import bstack111l1111l1_opy_, Events, bstack11l1l1l11l_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1l1llll1111_opy_, bstack1lll11l1lll_opy_, bstack1llll111111_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack111l1111l1_opy_ import bstack111l1111l1_opy_, Events, bstack11l1l1l11l_opy_
bstack1l111ll1l_opy_ = None
bstack11lllll1l1_opy_ = None
bstack1ll11l1l1l_opy_ = None
bstack1ll1lllll1_opy_ = None
bstack1l1llllll_opy_ = None
bstack11ll11lll1_opy_ = None
bstack111l1ll1l1_opy_ = None
bstack111lll11l1_opy_ = None
bstack1ll1111lll_opy_ = None
bstack11llllll11_opy_ = None
bstack1l1llll11l_opy_ = None
bstack111l111l11_opy_ = None
bstack1l11llllll_opy_ = None
bstack1lll1ll11l_opy_ = bstack111l1l_opy_ (u"ࠬ࠭≲")
CONFIG = {}
bstack11ll1l11ll_opy_ = False
bstack1l111l11l1_opy_ = bstack111l1l_opy_ (u"࠭ࠧ≳")
bstack1111l1111_opy_ = bstack111l1l_opy_ (u"ࠧࠨ≴")
bstack1llllll1l1_opy_ = False
bstack11llllll1_opy_ = []
bstack1ll1ll11l1_opy_ = bstack111l111ll1_opy_
bstack1lll1llll11l_opy_ = bstack111l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ≵")
bstack11lll11l11_opy_ = {}
bstack111l111l1l_opy_ = None
bstack11l1ll1lll_opy_ = False
logger = bstack1l11l1lll_opy_.get_logger(__name__, bstack1ll1ll11l1_opy_)
store = {
    bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭≶"): []
}
bstack1lll1lll1l1l_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1ll111ll_opy_ = {}
current_test_uuid = None
cli_context = bstack1l1llll1111_opy_(
    test_framework_name=bstack1l1l11111_opy_[bstack111l1l_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖ࠰ࡆࡉࡊࠧ≷")] if bstack111ll1llll_opy_() else bstack1l1l11111_opy_[bstack111l1l_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࠫ≸")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack1lll1l1111_opy_(page, bstack1l1ll11l11_opy_):
    try:
        page.evaluate(bstack111l1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ≹"),
                      bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪ≺") + json.dumps(
                          bstack1l1ll11l11_opy_) + bstack111l1l_opy_ (u"ࠢࡾࡿࠥ≻"))
    except Exception as e:
        print(bstack111l1l_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨ≼"), e)
def bstack111lll11ll_opy_(page, message, level):
    try:
        page.evaluate(bstack111l1l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ≽"), bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ≾") + json.dumps(
            message) + bstack111l1l_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧ≿") + json.dumps(level) + bstack111l1l_opy_ (u"ࠬࢃࡽࠨ⊀"))
    except Exception as e:
        print(bstack111l1l_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾࠤ⊁"), e)
def pytest_configure(config):
    global bstack1l111l11l1_opy_
    global CONFIG
    bstack1lllll1l1_opy_ = Config.bstack1111ll1l_opy_()
    config.args = bstack1lll1111_opy_.bstack11l111llll1_opy_(config.args)
    bstack1lllll1l1_opy_.bstack111lll1l11_opy_(bstack11l1llll1_opy_(config.getoption(bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ⊂"))))
    try:
        bstack1l11l1lll_opy_.bstack11111l111l1_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack111l1111l1_opy_.invoke(Events.CONNECT, bstack11l1l1l11l_opy_())
        cli_context.platform_index = int(os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ⊃"), bstack111l1l_opy_ (u"ࠩ࠳ࠫ⊄")))
        config = json.loads(os.environ.get(bstack111l1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠤ⊅"), bstack111l1l_opy_ (u"ࠦࢀࢃࠢ⊆")))
        cli.bstack1l11lll111l_opy_(bstack1lll11llll_opy_(bstack1l111l11l1_opy_, CONFIG), cli_context.platform_index, bstack1l1l1lll11_opy_)
    if cli.bstack1l1l1lllll1_opy_(bstack1l1l111ll1l_opy_):
        cli.bstack1l11lll11l1_opy_()
        logger.debug(bstack111l1l_opy_ (u"ࠧࡉࡌࡊࠢ࡬ࡷࠥࡧࡣࡵ࡫ࡹࡩࠥ࡬࡯ࡳࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࠦ⊇") + str(cli_context.platform_index) + bstack111l1l_opy_ (u"ࠨࠢ⊈"))
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.BEFORE_ALL, bstack1llll111111_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack111l1l_opy_ (u"ࠢࡸࡪࡨࡲࠧ⊉"), None)
    if cli.is_running() and when == bstack111l1l_opy_ (u"ࠣࡥࡤࡰࡱࠨ⊊"):
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.LOG_REPORT, bstack1llll111111_opy_.PRE, item, call)
    outcome = yield
    if when == bstack111l1l_opy_ (u"ࠤࡦࡥࡱࡲࠢ⊋"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111l1l_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧ⊌")))
        if not passed:
            config = json.loads(os.environ.get(bstack111l1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠥ⊍"), bstack111l1l_opy_ (u"ࠧࢁࡽࠣ⊎")))
            if bstack1llll1lll_opy_.bstack1llll1l11_opy_(config):
                bstack1lllllllllll_opy_ = bstack1llll1lll_opy_.bstack1111l111_opy_(config)
                if item.execution_count > bstack1lllllllllll_opy_:
                    print(bstack111l1l_opy_ (u"࠭ࡔࡦࡵࡷࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡦ࡬ࡴࡦࡴࠣࡶࡪࡺࡲࡪࡧࡶ࠾ࠥ࠭⊏"), report.nodeid, os.environ.get(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⊐")))
                    bstack1llll1lll_opy_.bstack111lll11l1l_opy_(report.nodeid)
            else:
                print(bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࠨ⊑"), report.nodeid, os.environ.get(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ⊒")))
                bstack1llll1lll_opy_.bstack111lll11l1l_opy_(report.nodeid)
        else:
            print(bstack111l1l_opy_ (u"ࠪࡘࡪࡹࡴࠡࡲࡤࡷࡸ࡫ࡤ࠻ࠢࠪ⊓"), report.nodeid, os.environ.get(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ⊔")))
    if cli.is_running():
        if when == bstack111l1l_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦ⊕"):
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.BEFORE_EACH, bstack1llll111111_opy_.POST, item, call, outcome)
        elif when == bstack111l1l_opy_ (u"ࠨࡣࡢ࡮࡯ࠦ⊖"):
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.LOG_REPORT, bstack1llll111111_opy_.POST, item, call, outcome)
        elif when == bstack111l1l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤ⊗"):
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.AFTER_EACH, bstack1llll111111_opy_.POST, item, call, outcome)
        return # skip all existing operations
    skipSessionName = item.config.getoption(bstack111l1l_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⊘"))
    plugins = item.config.getoption(bstack111l1l_opy_ (u"ࠤࡳࡰࡺ࡭ࡩ࡯ࡵࠥ⊙"))
    report = outcome.get_result()
    os.environ[bstack111l1l_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭⊚")] = report.nodeid
    bstack1lll1lll111l_opy_(item, call, report)
    if bstack111l1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠤ⊛") not in plugins or bstack111ll1llll_opy_():
        return
    summary = []
    driver = getattr(item, bstack111l1l_opy_ (u"ࠧࡥࡤࡳ࡫ࡹࡩࡷࠨ⊜"), None)
    page = getattr(item, bstack111l1l_opy_ (u"ࠨ࡟ࡱࡣࡪࡩࠧ⊝"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1lll1ll1l1ll_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1lll1lll11ll_opy_(item, report, summary, skipSessionName)
def bstack1lll1ll1l1ll_opy_(item, report, summary, skipSessionName):
    if report.when == bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⊞") and report.skipped:
        bstack11l111ll1ll_opy_(report)
    if report.when in [bstack111l1l_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢ⊟"), bstack111l1l_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦ⊠")]:
        return
    if not bstack1lll1l1111l_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack111l1l_opy_ (u"ࠪࡸࡷࡻࡥࠨ⊡")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ⊢") + json.dumps(
                    report.nodeid) + bstack111l1l_opy_ (u"ࠬࢃࡽࠨ⊣"))
        os.environ[bstack111l1l_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ⊤")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack111l1l_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦ࠼ࠣࡿ࠵ࢃࠢ⊥").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111l1l_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ⊦")))
    bstack1ll1l11l1_opy_ = bstack111l1l_opy_ (u"ࠤࠥ⊧")
    bstack11l111ll1ll_opy_(report)
    if not passed:
        try:
            bstack1ll1l11l1_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack111l1l_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥ⊨").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll1l11l1_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack111l1l_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨ⊩")))
        bstack1ll1l11l1_opy_ = bstack111l1l_opy_ (u"ࠧࠨ⊪")
        if not passed:
            try:
                bstack1ll1l11l1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111l1l_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨ⊫").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll1l11l1_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫ⊬")
                    + json.dumps(bstack111l1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠢࠤ⊭"))
                    + bstack111l1l_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧ⊮")
                )
            else:
                item._driver.execute_script(
                    bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨ⊯")
                    + json.dumps(str(bstack1ll1l11l1_opy_))
                    + bstack111l1l_opy_ (u"ࠦࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢ⊰")
                )
        except Exception as e:
            summary.append(bstack111l1l_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡥࡳࡴ࡯ࡵࡣࡷࡩ࠿ࠦࡻ࠱ࡿࠥ⊱").format(e))
def bstack1lll1ll1llll_opy_(test_name, error_message):
    try:
        bstack1lll1ll1lll1_opy_ = []
        bstack1l1lll11ll_opy_ = os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭⊲"), bstack111l1l_opy_ (u"ࠧ࠱ࠩ⊳"))
        bstack11l1ll1l11_opy_ = {bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭⊴"): test_name, bstack111l1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ⊵"): error_message, bstack111l1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ⊶"): bstack1l1lll11ll_opy_}
        bstack1lll1ll1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩ⊷"))
        if os.path.exists(bstack1lll1ll1l111_opy_):
            with open(bstack1lll1ll1l111_opy_) as f:
                bstack1lll1ll1lll1_opy_ = json.load(f)
        bstack1lll1ll1lll1_opy_.append(bstack11l1ll1l11_opy_)
        with open(bstack1lll1ll1l111_opy_, bstack111l1l_opy_ (u"ࠬࡽࠧ⊸")) as f:
            json.dump(bstack1lll1ll1lll1_opy_, f)
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡨࡶࡸ࡯ࡳࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡨࡶࡷࡵࡲࡴ࠼ࠣࠫ⊹") + str(e))
def bstack1lll1lll11ll_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack111l1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨ⊺"), bstack111l1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥ⊻")]:
        return
    if (str(skipSessionName).lower() != bstack111l1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⊼")):
        bstack1lll1l1111_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111l1l_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧ⊽")))
    bstack1ll1l11l1_opy_ = bstack111l1l_opy_ (u"ࠦࠧ⊾")
    bstack11l111ll1ll_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1ll1l11l1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111l1l_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧ⊿").format(e)
                )
        try:
            if passed:
                bstack1lll11lll1_opy_(getattr(item, bstack111l1l_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬ⋀"), None), bstack111l1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ⋁"))
            else:
                error_message = bstack111l1l_opy_ (u"ࠨࠩ⋂")
                if bstack1ll1l11l1_opy_:
                    bstack111lll11ll_opy_(item._page, str(bstack1ll1l11l1_opy_), bstack111l1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ⋃"))
                    bstack1lll11lll1_opy_(getattr(item, bstack111l1l_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩ⋄"), None), bstack111l1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ⋅"), str(bstack1ll1l11l1_opy_))
                    error_message = str(bstack1ll1l11l1_opy_)
                else:
                    bstack1lll11lll1_opy_(getattr(item, bstack111l1l_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫ⋆"), None), bstack111l1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ⋇"))
                bstack1lll1ll1llll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack111l1l_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡻࡰࡥࡣࡷࡩࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼ࠲ࢀࠦ⋈").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack111l1l_opy_ (u"ࠣ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ⋉"), default=bstack111l1l_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣ⋊"), help=bstack111l1l_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡨࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠤ⋋"))
    parser.addoption(bstack111l1l_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ⋌"), default=bstack111l1l_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦ⋍"), help=bstack111l1l_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧ⋎"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack111l1l_opy_ (u"ࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤ⋏"), action=bstack111l1l_opy_ (u"ࠣࡵࡷࡳࡷ࡫ࠢ⋐"), default=bstack111l1l_opy_ (u"ࠤࡦ࡬ࡷࡵ࡭ࡦࠤ⋑"),
                         help=bstack111l1l_opy_ (u"ࠥࡈࡷ࡯ࡶࡦࡴࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴࠤ⋒"))
def bstack1ll11l11_opy_(log):
    if not (log[bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⋓")] and log[bstack111l1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⋔")].strip()):
        return
    active = bstack1ll11111_opy_()
    log = {
        bstack111l1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⋕"): log[bstack111l1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⋖")],
        bstack111l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⋗"): bstack1l1ll111_opy_().isoformat() + bstack111l1l_opy_ (u"ࠩ࡝ࠫ⋘"),
        bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⋙"): log[bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⋚")],
    }
    if active:
        if active[bstack111l1l_opy_ (u"ࠬࡺࡹࡱࡧࠪ⋛")] == bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⋜"):
            log[bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⋝")] = active[bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⋞")]
        elif active[bstack111l1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⋟")] == bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࠨ⋠"):
            log[bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⋡")] = active[bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⋢")]
    bstack1l1l1111_opy_.bstack1ll1111l_opy_([log])
def bstack1ll11111_opy_():
    if len(store[bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⋣")]) > 0 and store[bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⋤")][-1]:
        return {
            bstack111l1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭⋥"): bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⋦"),
            bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⋧"): store[bstack111l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⋨")][-1]
        }
    if store.get(bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ⋩"), None):
        return {
            bstack111l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ⋪"): bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࠬ⋫"),
            bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⋬"): store[bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⋭")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.INIT_TEST, bstack1llll111111_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.INIT_TEST, bstack1llll111111_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.TEST, bstack1llll111111_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1lll1ll1ll11_opy_ = True
        bstack1111lllll1_opy_ = bstack1lll11ll1_opy_.bstack1l1ll11lll_opy_(bstack1111ll1ll11_opy_(item.own_markers))
        if not cli.bstack1l1l1lllll1_opy_(bstack1l1l111ll1l_opy_):
            item._a11y_test_case = bstack1111lllll1_opy_
            if bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ⋮"), None):
                driver = getattr(item, bstack111l1l_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ⋯"), None)
                item._a11y_started = bstack1lll11ll1_opy_.bstack1lll1lll11_opy_(driver, bstack1111lllll1_opy_)
        if not bstack1l1l1111_opy_.on() or bstack1lll1llll11l_opy_ != bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ⋰"):
            return
        global current_test_uuid #, bstack1l11ll1l_opy_
        bstack1ll1l11l_opy_ = {
            bstack111l1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⋱"): uuid4().__str__(),
            bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⋲"): bstack1l1ll111_opy_().isoformat() + bstack111l1l_opy_ (u"ࠨ࡜ࠪ⋳")
        }
        current_test_uuid = bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⋴")]
        store[bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⋵")] = bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩ⋶")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1ll111ll_opy_[item.nodeid] = {**_1ll111ll_opy_[item.nodeid], **bstack1ll1l11l_opy_}
        bstack1lll1lll1ll1_opy_(item, _1ll111ll_opy_[item.nodeid], bstack111l1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⋷"))
    except Exception as err:
        print(bstack111l1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡣࡢ࡮࡯࠾ࠥࢁࡽࠨ⋸"), str(err))
def pytest_runtest_setup(item):
    store[bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⋹")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.BEFORE_EACH, bstack1llll111111_opy_.PRE, item, bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⋺"))
    if bstack1llll1lll_opy_.bstack11l1111ll11_opy_():
            bstack1lll1lll1111_opy_ = bstack111l1l_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡤࡷࠥࡺࡨࡦࠢࡤࡦࡴࡸࡴࠡࡤࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠨ⋻")
            logger.error(bstack1lll1lll1111_opy_)
            bstack1ll1l11l_opy_ = {
                bstack111l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⋼"): uuid4().__str__(),
                bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⋽"): bstack1l1ll111_opy_().isoformat() + bstack111l1l_opy_ (u"ࠬࡠࠧ⋾"),
                bstack111l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⋿"): bstack1l1ll111_opy_().isoformat() + bstack111l1l_opy_ (u"࡛ࠧࠩ⌀"),
                bstack111l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⌁"): bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ⌂"),
                bstack111l1l_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ⌃"): bstack1lll1lll1111_opy_,
                bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⌄"): [],
                bstack111l1l_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ⌅"): []
            }
            bstack1lll1lll1ll1_opy_(item, bstack1ll1l11l_opy_, bstack111l1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧ⌆"))
            pytest.skip(bstack1lll1lll1111_opy_)
            return # skip all existing operations
    global bstack1lll1lll1l1l_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111l1l111l1_opy_():
        atexit.register(bstack1111l1111l_opy_)
        if not bstack1lll1lll1l1l_opy_:
            try:
                bstack1lll1ll11lll_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack1111llll11l_opy_():
                    bstack1lll1ll11lll_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1ll11lll_opy_:
                    signal.signal(s, bstack1llll1111111_opy_)
                bstack1lll1lll1l1l_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack111l1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩ࡬࡯ࡳࡵࡧࡵࠤࡸ࡯ࡧ࡯ࡣ࡯ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶࡸࡀࠠࠣ⌇") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l111ll1l1_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack111l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⌈")
    try:
        if not bstack1l1l1111_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack1ll1l11l_opy_ = {
            bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⌉"): uuid,
            bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⌊"): bstack1l1ll111_opy_().isoformat() + bstack111l1l_opy_ (u"ࠫ࡟࠭⌋"),
            bstack111l1l_opy_ (u"ࠬࡺࡹࡱࡧࠪ⌌"): bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⌍"),
            bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ⌎"): bstack111l1l_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭⌏"),
            bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬ⌐"): bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ⌑")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack111l1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ⌒")] = item
        store[bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⌓")] = [uuid]
        if not _1ll111ll_opy_.get(item.nodeid, None):
            _1ll111ll_opy_[item.nodeid] = {bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⌔"): [], bstack111l1l_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⌕"): []}
        _1ll111ll_opy_[item.nodeid][bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⌖")].append(bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⌗")])
        _1ll111ll_opy_[item.nodeid + bstack111l1l_opy_ (u"ࠪ࠱ࡸ࡫ࡴࡶࡲࠪ⌘")] = bstack1ll1l11l_opy_
        bstack1lll1lllllll_opy_(item, bstack1ll1l11l_opy_, bstack111l1l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⌙"))
    except Exception as err:
        print(bstack111l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨ⌚"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.TEST, bstack1llll111111_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.AFTER_EACH, bstack1llll111111_opy_.PRE, item, bstack111l1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ⌛"))
        return # skip all existing operations
    try:
        global bstack11lll11l11_opy_
        bstack1l1lll11ll_opy_ = 0
        if bstack1llllll1l1_opy_ is True:
            bstack1l1lll11ll_opy_ = int(os.environ.get(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ⌜")))
        if bstack1ll1111ll_opy_.bstack111llll1ll_opy_() == bstack111l1l_opy_ (u"ࠣࡶࡵࡹࡪࠨ⌝"):
            if bstack1ll1111ll_opy_.bstack1l1ll1lll1_opy_() == bstack111l1l_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦ⌞"):
                bstack1lll1ll1l1l1_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⌟"), None)
                bstack1111ll111l_opy_ = bstack1lll1ll1l1l1_opy_ + bstack111l1l_opy_ (u"ࠦ࠲ࡺࡥࡴࡶࡦࡥࡸ࡫ࠢ⌠")
                driver = getattr(item, bstack111l1l_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭⌡"), None)
                bstack1l11ll1l1_opy_ = getattr(item, bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⌢"), None)
                bstack11l1ll11l_opy_ = getattr(item, bstack111l1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⌣"), None)
                PercySDK.screenshot(driver, bstack1111ll111l_opy_, bstack1l11ll1l1_opy_=bstack1l11ll1l1_opy_, bstack11l1ll11l_opy_=bstack11l1ll11l_opy_, bstack1lll1ll1ll_opy_=bstack1l1lll11ll_opy_)
        if not cli.bstack1l1l1lllll1_opy_(bstack1l1l111ll1l_opy_):
            if getattr(item, bstack111l1l_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠨ⌤"), False):
                bstack111l1lll_opy_.bstack1lll1l111_opy_(getattr(item, bstack111l1l_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ⌥"), None), bstack11lll11l11_opy_, logger, item)
        if not bstack1l1l1111_opy_.on():
            return
        bstack1ll1l11l_opy_ = {
            bstack111l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⌦"): uuid4().__str__(),
            bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⌧"): bstack1l1ll111_opy_().isoformat() + bstack111l1l_opy_ (u"ࠬࡠࠧ⌨"),
            bstack111l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ〈"): bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ〉"),
            bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ⌫"): bstack111l1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭⌬"),
            bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭⌭"): bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭⌮")
        }
        _1ll111ll_opy_[item.nodeid + bstack111l1l_opy_ (u"ࠬ࠳ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ⌯")] = bstack1ll1l11l_opy_
        bstack1lll1lllllll_opy_(item, bstack1ll1l11l_opy_, bstack111l1l_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⌰"))
    except Exception as err:
        print(bstack111l1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯࠼ࠣࡿࢂ࠭⌱"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l111l1lll_opy_(fixturedef.argname):
        store[bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧ⌲")] = request.node
    elif bstack11l111l11l1_opy_(fixturedef.argname):
        store[bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡧࡱࡧࡳࡴࡡ࡬ࡸࡪࡳࠧ⌳")] = request.node
    if not bstack1l1l1111_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.SETUP_FIXTURE, bstack1llll111111_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.SETUP_FIXTURE, bstack1llll111111_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.SETUP_FIXTURE, bstack1llll111111_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.SETUP_FIXTURE, bstack1llll111111_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    try:
        fixture = {
            bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ⌴"): fixturedef.argname,
            bstack111l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⌵"): bstack1111lll1lll_opy_(outcome),
            bstack111l1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⌶"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⌷")]
        if not _1ll111ll_opy_.get(current_test_item.nodeid, None):
            _1ll111ll_opy_[current_test_item.nodeid] = {bstack111l1l_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⌸"): []}
        _1ll111ll_opy_[current_test_item.nodeid][bstack111l1l_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ⌹")].append(fixture)
    except Exception as err:
        logger.debug(bstack111l1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡶࡩࡹࡻࡰ࠻ࠢࡾࢁࠬ⌺"), str(err))
if bstack111ll1llll_opy_() and bstack1l1l1111_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.STEP, bstack1llll111111_opy_.PRE, request, step)
            return
        try:
            _1ll111ll_opy_[request.node.nodeid][bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⌻")].bstack11l111l1_opy_(id(step))
        except Exception as err:
            print(bstack111l1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴ࠿ࠦࡻࡾࠩ⌼"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.STEP, bstack1llll111111_opy_.POST, request, step, exception)
            return
        try:
            _1ll111ll_opy_[request.node.nodeid][bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ⌽")].bstack1lll1lll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack111l1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡶࡸࡪࡶ࡟ࡦࡴࡵࡳࡷࡀࠠࡼࡿࠪ⌾"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.STEP, bstack1llll111111_opy_.POST, request, step)
            return
        try:
            bstack1l1l11ll_opy_: bstack1l1l1ll1_opy_ = _1ll111ll_opy_[request.node.nodeid][bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ⌿")]
            bstack1l1l11ll_opy_.bstack1lll1lll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack111l1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡸࡺࡥࡱࡡࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠬ⍀"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1llll11l_opy_
        try:
            if not bstack1l1l1111_opy_.on() or bstack1lll1llll11l_opy_ != bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭⍁"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.TEST, bstack1llll111111_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ⍂"), None)
            if not _1ll111ll_opy_.get(request.node.nodeid, None):
                _1ll111ll_opy_[request.node.nodeid] = {}
            bstack1l1l11ll_opy_ = bstack1l1l1ll1_opy_.bstack111111l1111_opy_(
                scenario, feature, request.node,
                name=bstack11l111l1ll1_opy_(request.node, scenario),
                started_at=bstack1lllll11_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack111l1l_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭⍃"),
                tags=bstack11l111l1l1l_opy_(feature, scenario),
                bstack1llll11l_opy_=bstack1l1l1111_opy_.bstack1ll1l1ll_opy_(driver) if driver and driver.session_id else {}
            )
            _1ll111ll_opy_[request.node.nodeid][bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ⍄")] = bstack1l1l11ll_opy_
            bstack1lll1lll1lll_opy_(bstack1l1l11ll_opy_.uuid)
            bstack1l1l1111_opy_.bstack1l1l111l_opy_(bstack111l1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⍅"), bstack1l1l11ll_opy_)
        except Exception as err:
            print(bstack111l1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳ࠿ࠦࡻࡾࠩ⍆"), str(err))
def bstack1lll1lllll11_opy_(bstack11l1l1l1_opy_):
    if bstack11l1l1l1_opy_ in store[bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⍇")]:
        store[bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⍈")].remove(bstack11l1l1l1_opy_)
def bstack1lll1lll1lll_opy_(test_uuid):
    store[bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⍉")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1l1l1111_opy_.bstack1llll11llll1_opy_
def bstack1lll1lll111l_opy_(item, call, report):
    logger.debug(bstack111l1l_opy_ (u"ࠫ࡭ࡧ࡮ࡥ࡮ࡨࡣࡴ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡴࡶࡤࡶࡹ࠭⍊"))
    global bstack1lll1llll11l_opy_
    bstack1ll11l111_opy_ = bstack1lllll11_opy_()
    if hasattr(report, bstack111l1l_opy_ (u"ࠬࡹࡴࡰࡲࠪ⍋")):
        bstack1ll11l111_opy_ = bstack1111lllll1l_opy_(report.stop)
    elif hasattr(report, bstack111l1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࠬ⍌")):
        bstack1ll11l111_opy_ = bstack1111lllll1l_opy_(report.start)
    try:
        if getattr(report, bstack111l1l_opy_ (u"ࠧࡸࡪࡨࡲࠬ⍍"), bstack111l1l_opy_ (u"ࠨࠩ⍎")) == bstack111l1l_opy_ (u"ࠩࡦࡥࡱࡲࠧ⍏"):
            logger.debug(bstack111l1l_opy_ (u"ࠪ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡳࡵࡣࡷࡩࠥ࠳ࠠࡼࡿ࠯ࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠ࠮ࠢࡾࢁࠬ⍐").format(getattr(report, bstack111l1l_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⍑"), bstack111l1l_opy_ (u"ࠬ࠭⍒")).__str__(), bstack1lll1llll11l_opy_))
            if bstack1lll1llll11l_opy_ == bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭⍓"):
                _1ll111ll_opy_[item.nodeid][bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⍔")] = bstack1ll11l111_opy_
                bstack1lll1lll1ll1_opy_(item, _1ll111ll_opy_[item.nodeid], bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⍕"), report, call)
                store[bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⍖")] = None
            elif bstack1lll1llll11l_opy_ == bstack111l1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢ⍗"):
                bstack1l1l11ll_opy_ = _1ll111ll_opy_[item.nodeid][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⍘")]
                bstack1l1l11ll_opy_.set(hooks=_1ll111ll_opy_[item.nodeid].get(bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⍙"), []))
                exception, bstack11lll111_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11lll111_opy_ = [call.excinfo.exconly(), getattr(report, bstack111l1l_opy_ (u"࠭࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠬ⍚"), bstack111l1l_opy_ (u"ࠧࠨ⍛"))]
                bstack1l1l11ll_opy_.stop(time=bstack1ll11l111_opy_, result=Result(result=getattr(report, bstack111l1l_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩ⍜"), bstack111l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⍝")), exception=exception, bstack11lll111_opy_=bstack11lll111_opy_))
                bstack1l1l1111_opy_.bstack1l1l111l_opy_(bstack111l1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⍞"), _1ll111ll_opy_[item.nodeid][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⍟")])
        elif getattr(report, bstack111l1l_opy_ (u"ࠬࡽࡨࡦࡰࠪ⍠"), bstack111l1l_opy_ (u"࠭ࠧ⍡")) in [bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⍢"), bstack111l1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪ⍣")]:
            logger.debug(bstack111l1l_opy_ (u"ࠩ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡹࡴࡢࡶࡨࠤ࠲ࠦࡻࡾ࠮ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦ࠭ࠡࡽࢀࠫ⍤").format(getattr(report, bstack111l1l_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⍥"), bstack111l1l_opy_ (u"ࠫࠬ⍦")).__str__(), bstack1lll1llll11l_opy_))
            bstack1l11l1l1_opy_ = item.nodeid + bstack111l1l_opy_ (u"ࠬ࠳ࠧ⍧") + getattr(report, bstack111l1l_opy_ (u"࠭ࡷࡩࡧࡱࠫ⍨"), bstack111l1l_opy_ (u"ࠧࠨ⍩"))
            if getattr(report, bstack111l1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ⍪"), False):
                hook_type = bstack111l1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧ⍫") if getattr(report, bstack111l1l_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⍬"), bstack111l1l_opy_ (u"ࠫࠬ⍭")) == bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ⍮") else bstack111l1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ⍯")
                _1ll111ll_opy_[bstack1l11l1l1_opy_] = {
                    bstack111l1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⍰"): uuid4().__str__(),
                    bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⍱"): bstack1ll11l111_opy_,
                    bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬ⍲"): hook_type
                }
            _1ll111ll_opy_[bstack1l11l1l1_opy_][bstack111l1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⍳")] = bstack1ll11l111_opy_
            bstack1lll1lllll11_opy_(_1ll111ll_opy_[bstack1l11l1l1_opy_][bstack111l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩ⍴")])
            bstack1lll1lllllll_opy_(item, _1ll111ll_opy_[bstack1l11l1l1_opy_], bstack111l1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⍵"), report, call)
            if getattr(report, bstack111l1l_opy_ (u"࠭ࡷࡩࡧࡱࠫ⍶"), bstack111l1l_opy_ (u"ࠧࠨ⍷")) == bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⍸"):
                if getattr(report, bstack111l1l_opy_ (u"ࠩࡲࡹࡹࡩ࡯࡮ࡧࠪ⍹"), bstack111l1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ⍺")) == bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⍻"):
                    bstack1ll1l11l_opy_ = {
                        bstack111l1l_opy_ (u"ࠬࡻࡵࡪࡦࠪ⍼"): uuid4().__str__(),
                        bstack111l1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⍽"): bstack1lllll11_opy_(),
                        bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⍾"): bstack1lllll11_opy_()
                    }
                    _1ll111ll_opy_[item.nodeid] = {**_1ll111ll_opy_[item.nodeid], **bstack1ll1l11l_opy_}
                    bstack1lll1lll1ll1_opy_(item, _1ll111ll_opy_[item.nodeid], bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⍿"))
                    bstack1lll1lll1ll1_opy_(item, _1ll111ll_opy_[item.nodeid], bstack111l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⎀"), report, call)
    except Exception as err:
        print(bstack111l1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࢁࡽࠨ⎁"), str(err))
def bstack1lll1llllll1_opy_(test, bstack1ll1l11l_opy_, result=None, call=None, bstack1111l11ll_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l1l11ll_opy_ = {
        bstack111l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩ⎂"): bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠬࡻࡵࡪࡦࠪ⎃")],
        bstack111l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ⎄"): bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࠬ⎅"),
        bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭⎆"): test.name,
        bstack111l1l_opy_ (u"ࠩࡥࡳࡩࡿࠧ⎇"): {
            bstack111l1l_opy_ (u"ࠪࡰࡦࡴࡧࠨ⎈"): bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ⎉"),
            bstack111l1l_opy_ (u"ࠬࡩ࡯ࡥࡧࠪ⎊"): inspect.getsource(test.obj)
        },
        bstack111l1l_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ⎋"): test.name,
        bstack111l1l_opy_ (u"ࠧࡴࡥࡲࡴࡪ࠭⎌"): test.name,
        bstack111l1l_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨ⎍"): bstack1lll1111_opy_.bstack1l11l11l_opy_(test),
        bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ⎎"): file_path,
        bstack111l1l_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬ⎏"): file_path,
        bstack111l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⎐"): bstack111l1l_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭⎑"),
        bstack111l1l_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫ⎒"): file_path,
        bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⎓"): bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⎔")],
        bstack111l1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ⎕"): bstack111l1l_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪ⎖"),
        bstack111l1l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳࠧ⎗"): {
            bstack111l1l_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩ⎘"): test.nodeid
        },
        bstack111l1l_opy_ (u"࠭ࡴࡢࡩࡶࠫ⎙"): bstack1111ll1ll11_opy_(test.own_markers)
    }
    if bstack1111l11ll_opy_ in [bstack111l1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ⎚"), bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⎛")]:
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠩࡰࡩࡹࡧࠧ⎜")] = {
            bstack111l1l_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ⎝"): bstack1ll1l11l_opy_.get(bstack111l1l_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭⎞"), [])
        }
    if bstack1111l11ll_opy_ == bstack111l1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭⎟"):
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⎠")] = bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⎡")
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⎢")] = bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⎣")]
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⎤")] = bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⎥")]
    if result:
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⎦")] = result.outcome
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ⎧")] = result.duration * 1000
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎨")] = bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⎩")]
        if result.failed:
            bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ⎪")] = bstack1l1l1111_opy_.bstack1111111l1l_opy_(call.excinfo.typename)
            bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ⎫")] = bstack1l1l1111_opy_.bstack1llll11l1111_opy_(call.excinfo, result)
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⎬")] = bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⎭")]
    if outcome:
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⎮")] = bstack1111lll1lll_opy_(outcome)
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ⎯")] = 0
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⎰")] = bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⎱")]
        if bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⎲")] == bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⎳"):
            bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ⎴")] = bstack111l1l_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧ⎵")  # bstack1lll1ll11ll1_opy_
            bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ⎶")] = [{bstack111l1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ⎷"): [bstack111l1l_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭⎸")]}]
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⎹")] = bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⎺")]
    return bstack1l1l11ll_opy_
def bstack1lll1ll1ll1l_opy_(test, bstack1llll1l1_opy_, bstack1111l11ll_opy_, result, call, outcome, bstack1lll1llll1l1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1llll1l1_opy_[bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⎻")]
    hook_name = bstack1llll1l1_opy_[bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ⎼")]
    hook_data = {
        bstack111l1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⎽"): bstack1llll1l1_opy_[bstack111l1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⎾")],
        bstack111l1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⎿"): bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ⏀"),
        bstack111l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⏁"): bstack111l1l_opy_ (u"ࠬࢁࡽࠨ⏂").format(bstack11l111ll111_opy_(hook_name)),
        bstack111l1l_opy_ (u"࠭ࡢࡰࡦࡼࠫ⏃"): {
            bstack111l1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬ⏄"): bstack111l1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ⏅"),
            bstack111l1l_opy_ (u"ࠩࡦࡳࡩ࡫ࠧ⏆"): None
        },
        bstack111l1l_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩ⏇"): test.name,
        bstack111l1l_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫ⏈"): bstack1lll1111_opy_.bstack1l11l11l_opy_(test, hook_name),
        bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ⏉"): file_path,
        bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨ⏊"): file_path,
        bstack111l1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⏋"): bstack111l1l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⏌"),
        bstack111l1l_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧ⏍"): file_path,
        bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⏎"): bstack1llll1l1_opy_[bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⏏")],
        bstack111l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ⏐"): bstack111l1l_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨ⏑") if bstack1lll1llll11l_opy_ == bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫ⏒") else bstack111l1l_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ⏓"),
        bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬ⏔"): hook_type
    }
    bstack1l111l1l11l_opy_ = bstack11lll1l1_opy_(_1ll111ll_opy_.get(test.nodeid, None))
    if bstack1l111l1l11l_opy_:
        hook_data[bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡯ࡤࠨ⏕")] = bstack1l111l1l11l_opy_
    if result:
        hook_data[bstack111l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⏖")] = result.outcome
        hook_data[bstack111l1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭⏗")] = result.duration * 1000
        hook_data[bstack111l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⏘")] = bstack1llll1l1_opy_[bstack111l1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⏙")]
        if result.failed:
            hook_data[bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⏚")] = bstack1l1l1111_opy_.bstack1111111l1l_opy_(call.excinfo.typename)
            hook_data[bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ⏛")] = bstack1l1l1111_opy_.bstack1llll11l1111_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack111l1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⏜")] = bstack1111lll1lll_opy_(outcome)
        hook_data[bstack111l1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⏝")] = 100
        hook_data[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏞")] = bstack1llll1l1_opy_[bstack111l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⏟")]
        if hook_data[bstack111l1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⏠")] == bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ⏡"):
            hook_data[bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ⏢")] = bstack111l1l_opy_ (u"࡙ࠪࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠫ⏣")  # bstack1lll1ll11ll1_opy_
            hook_data[bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ⏤")] = [{bstack111l1l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ⏥"): [bstack111l1l_opy_ (u"࠭ࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠪ⏦")]}]
    if bstack1lll1llll1l1_opy_:
        hook_data[bstack111l1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⏧")] = bstack1lll1llll1l1_opy_.result
        hook_data[bstack111l1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩ⏨")] = bstack111l1ll1ll1_opy_(bstack1llll1l1_opy_[bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⏩")], bstack1llll1l1_opy_[bstack111l1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⏪")])
        hook_data[bstack111l1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏫")] = bstack1llll1l1_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏬")]
        if hook_data[bstack111l1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⏭")] == bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⏮"):
            hook_data[bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⏯")] = bstack1l1l1111_opy_.bstack1111111l1l_opy_(bstack1lll1llll1l1_opy_.exception_type)
            hook_data[bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ⏰")] = [{bstack111l1l_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭⏱"): bstack111l1l11ll1_opy_(bstack1lll1llll1l1_opy_.exception)}]
    return hook_data
def bstack1lll1lll1ll1_opy_(test, bstack1ll1l11l_opy_, bstack1111l11ll_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack111l1l_opy_ (u"ࠫࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡴࡦࡵࡷࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠣ࠱ࠥࢁࡽࠨ⏲").format(bstack1111l11ll_opy_))
    bstack1l1l11ll_opy_ = bstack1lll1llllll1_opy_(test, bstack1ll1l11l_opy_, result, call, bstack1111l11ll_opy_, outcome)
    driver = getattr(test, bstack111l1l_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭⏳"), None)
    if bstack1111l11ll_opy_ == bstack111l1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⏴") and driver:
        bstack1l1l11ll_opy_[bstack111l1l_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭⏵")] = bstack1l1l1111_opy_.bstack1ll1l1ll_opy_(driver)
    if bstack1111l11ll_opy_ == bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩ⏶"):
        bstack1111l11ll_opy_ = bstack111l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⏷")
    bstack1l111lll_opy_ = {
        bstack111l1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⏸"): bstack1111l11ll_opy_,
        bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⏹"): bstack1l1l11ll_opy_
    }
    bstack1l1l1111_opy_.bstack1lll1l1l_opy_(bstack1l111lll_opy_)
    if bstack1111l11ll_opy_ == bstack111l1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⏺"):
        threading.current_thread().bstackTestMeta = {bstack111l1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⏻"): bstack111l1l_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ⏼")}
    elif bstack1111l11ll_opy_ == bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⏽"):
        threading.current_thread().bstackTestMeta = {bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ⏾"): getattr(result, bstack111l1l_opy_ (u"ࠪࡳࡺࡺࡣࡰ࡯ࡨࠫ⏿"), bstack111l1l_opy_ (u"ࠫࠬ␀"))}
def bstack1lll1lllllll_opy_(test, bstack1ll1l11l_opy_, bstack1111l11ll_opy_, result=None, call=None, outcome=None, bstack1lll1llll1l1_opy_=None):
    logger.debug(bstack111l1l_opy_ (u"ࠬࡹࡥ࡯ࡦࡢ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡩࡱࡲ࡯ࠥࡪࡡࡵࡣ࠯ࠤࡪࡼࡥ࡯ࡶࡗࡽࡵ࡫ࠠ࠮ࠢࡾࢁࠬ␁").format(bstack1111l11ll_opy_))
    hook_data = bstack1lll1ll1ll1l_opy_(test, bstack1ll1l11l_opy_, bstack1111l11ll_opy_, result, call, outcome, bstack1lll1llll1l1_opy_)
    bstack1l111lll_opy_ = {
        bstack111l1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ␂"): bstack1111l11ll_opy_,
        bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩ␃"): hook_data
    }
    bstack1l1l1111_opy_.bstack1lll1l1l_opy_(bstack1l111lll_opy_)
def bstack11lll1l1_opy_(bstack1ll1l11l_opy_):
    if not bstack1ll1l11l_opy_:
        return None
    if bstack1ll1l11l_opy_.get(bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ␄"), None):
        return getattr(bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ␅")], bstack111l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ␆"), None)
    return bstack1ll1l11l_opy_.get(bstack111l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩ␇"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.LOG, bstack1llll111111_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_.LOG, bstack1llll111111_opy_.POST, request, caplog)
        return # skip all existing operations
    try:
        if not bstack1l1l1111_opy_.on():
            return
        places = [bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ␈"), bstack111l1l_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ␉"), bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ␊")]
        logs = []
        for bstack1lll1llll111_opy_ in places:
            records = caplog.get_records(bstack1lll1llll111_opy_)
            bstack1lll1llll1ll_opy_ = bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ␋") if bstack1lll1llll111_opy_ == bstack111l1l_opy_ (u"ࠩࡦࡥࡱࡲࠧ␌") else bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ␍")
            bstack1lll1ll111ll_opy_ = request.node.nodeid + (bstack111l1l_opy_ (u"ࠫࠬ␎") if bstack1lll1llll111_opy_ == bstack111l1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ␏") else bstack111l1l_opy_ (u"࠭࠭ࠨ␐") + bstack1lll1llll111_opy_)
            test_uuid = bstack11lll1l1_opy_(_1ll111ll_opy_.get(bstack1lll1ll111ll_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack1111l11ll11_opy_(record.message):
                    continue
                logs.append({
                    bstack111l1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ␑"): bstack1111ll111ll_opy_(record.created).isoformat() + bstack111l1l_opy_ (u"ࠨ࡜ࠪ␒"),
                    bstack111l1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ␓"): record.levelname,
                    bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ␔"): record.message,
                    bstack1lll1llll1ll_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1l1l1111_opy_.bstack1ll1111l_opy_(logs)
    except Exception as err:
        print(bstack111l1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡩ࡯࡯ࡦࡢࡪ࡮ࡾࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ␕"), str(err))
def bstack1ll1ll1l11_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack11l1ll1lll_opy_
    bstack11111l11l1_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ␖"), None) and bstack1l11l1ll_opy_(
            threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ␗"), None)
    bstack1l11l1111_opy_ = getattr(driver, bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ␘"), None) != None and getattr(driver, bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ␙"), None) == True
    if sequence == bstack111l1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ␚") and driver != None:
      if not bstack11l1ll1lll_opy_ and bstack1lll1l1111l_opy_() and bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ␛") in CONFIG and CONFIG[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ␜")] == True and bstack111ll11l11_opy_.bstack11llll1ll1_opy_(driver_command) and (bstack1l11l1111_opy_ or bstack11111l11l1_opy_) and not bstack1l11l1111l_opy_(args):
        try:
          bstack11l1ll1lll_opy_ = True
          logger.debug(bstack111l1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧ␝").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack111l1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫ␞").format(str(err)))
        bstack11l1ll1lll_opy_ = False
    if sequence == bstack111l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭␟"):
        if driver_command == bstack111l1l_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ␠"):
            bstack1l1l1111_opy_.bstack11111l1ll_opy_({
                bstack111l1l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ␡"): response[bstack111l1l_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ␢")],
                bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ␣"): store[bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ␤")]
            })
def bstack1111l1111l_opy_():
    global bstack11llllll1_opy_
    bstack1l11l1lll_opy_.bstack111l1ll1l_opy_()
    logging.shutdown()
    bstack1l1l1111_opy_.bstack1l1l1lll_opy_()
    for driver in bstack11llllll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1llll1111111_opy_(*args):
    global bstack11llllll1_opy_
    bstack1l1l1111_opy_.bstack1l1l1lll_opy_()
    for driver in bstack11llllll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1lllll1ll1_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1l1l1ll1ll_opy_(self, *args, **kwargs):
    bstack1l111ll1ll_opy_ = bstack1l111ll1l_opy_(self, *args, **kwargs)
    bstack111l1l1l1_opy_ = getattr(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧ␥"), None)
    if bstack111l1l1l1_opy_ and bstack111l1l1l1_opy_.get(bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ␦"), bstack111l1l_opy_ (u"ࠨࠩ␧")) == bstack111l1l_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪ␨"):
        bstack1l1l1111_opy_.bstack1l1l1111l1_opy_(self)
    return bstack1l111ll1ll_opy_
@measure(event_name=EVENTS.bstack111l1ll1ll_opy_, stage=STAGE.bstack11ll1l111l_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1l111llll_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1lllll1l1_opy_ = Config.bstack1111ll1l_opy_()
    if bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧ␩")):
        return
    bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨ␪"), True)
    global bstack1lll1ll11l_opy_
    global bstack11l1l1l11_opy_
    bstack1lll1ll11l_opy_ = framework_name
    logger.info(bstack11l11111l_opy_.format(bstack1lll1ll11l_opy_.split(bstack111l1l_opy_ (u"ࠬ࠳ࠧ␫"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1lll1l1111l_opy_():
            Service.start = bstack11ll111l11_opy_
            Service.stop = bstack1lllll111l_opy_
            webdriver.Remote.get = bstack1ll1l1l1l_opy_
            webdriver.Remote.__init__ = bstack1ll11ll11l_opy_
            if not isinstance(os.getenv(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡁࡓࡃࡏࡐࡊࡒࠧ␬")), str):
                return
            WebDriver.quit = bstack1ll1l1l11l_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1l1l1111_opy_.on():
            webdriver.Remote.__init__ = bstack1l1l1ll1ll_opy_
        bstack11l1l1l11_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack111l1l_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬ␭")):
        bstack11l1l1l11_opy_ = eval(os.environ.get(bstack111l1l_opy_ (u"ࠨࡕࡈࡐࡊࡔࡉࡖࡏࡢࡓࡗࡥࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡍࡓ࡙ࡔࡂࡎࡏࡉࡉ࠭␮")))
    if not bstack11l1l1l11_opy_:
        bstack1l11l1l1ll_opy_(bstack111l1l_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ␯"), bstack111l1l11l_opy_)
    if bstack11l1l11ll1_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack111l1l_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ␰")) and callable(getattr(RemoteConnection, bstack111l1l_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ␱"))):
                RemoteConnection._get_proxy_url = bstack11ll1lll1_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack11ll1lll1_opy_
        except Exception as e:
            logger.error(bstack1ll1l1ll11_opy_.format(str(e)))
    if bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ␲") in str(framework_name).lower():
        if not bstack1lll1l1111l_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack11l1ll1111_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11ll111l1_opy_
            Config.getoption = bstack1l1l1111ll_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack111111ll1l_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1lll1lll1l_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll1l1l11l_opy_(self):
    global bstack1lll1ll11l_opy_
    global bstack11lll11l1l_opy_
    global bstack11lllll1l1_opy_
    try:
        if bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭␳") in bstack1lll1ll11l_opy_ and self.session_id != None and bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫ␴"), bstack111l1l_opy_ (u"ࠨࠩ␵")) != bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ␶"):
            bstack1lllll11ll_opy_ = bstack111l1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ␷") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ␸")
            bstack111l11ll1_opy_(logger, True)
            if os.environ.get(bstack111l1l_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ␹"), None):
                self.execute_script(
                    bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ␺") + json.dumps(
                        os.environ.get(bstack111l1l_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪ␻"))) + bstack111l1l_opy_ (u"ࠨࡿࢀࠫ␼"))
            if self != None:
                bstack11ll1111l1_opy_(self, bstack1lllll11ll_opy_, bstack111l1l_opy_ (u"ࠩ࠯ࠤࠬ␽").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1l1l1lllll1_opy_(bstack1l1l111ll1l_opy_):
            item = store.get(bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ␾"), None)
            if item is not None and bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ␿"), None):
                bstack111l1lll_opy_.bstack1lll1l111_opy_(self, bstack11lll11l11_opy_, logger, item)
        threading.current_thread().testStatus = bstack111l1l_opy_ (u"ࠬ࠭⑀")
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢ⑁") + str(e))
    bstack11lllll1l1_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1lll11111l_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll11ll11l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack11lll11l1l_opy_
    global bstack111l111l1l_opy_
    global bstack1llllll1l1_opy_
    global bstack1lll1ll11l_opy_
    global bstack1l111ll1l_opy_
    global bstack11llllll1_opy_
    global bstack1l111l11l1_opy_
    global bstack1111l1111_opy_
    global bstack11lll11l11_opy_
    CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ⑂")] = str(bstack1lll1ll11l_opy_) + str(__version__)
    command_executor = bstack1lll11llll_opy_(bstack1l111l11l1_opy_, CONFIG)
    logger.debug(bstack11l1llll1l_opy_.format(command_executor))
    proxy = bstack1l1lllll1_opy_(CONFIG, proxy)
    bstack1l1lll11ll_opy_ = 0
    try:
        if bstack1llllll1l1_opy_ is True:
            bstack1l1lll11ll_opy_ = int(os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ⑃")))
    except:
        bstack1l1lll11ll_opy_ = 0
    bstack1111ll1111_opy_ = bstack1l11ll1l1l_opy_(CONFIG, bstack1l1lll11ll_opy_)
    logger.debug(bstack11l1llllll_opy_.format(str(bstack1111ll1111_opy_)))
    bstack11lll11l11_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⑄"))[bstack1l1lll11ll_opy_]
    if bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ⑅") in CONFIG and CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ⑆")]:
        bstack1ll1l11ll_opy_(bstack1111ll1111_opy_, bstack1111l1111_opy_)
    if bstack1lll11ll1_opy_.bstack1l1l1111l_opy_(CONFIG, bstack1l1lll11ll_opy_) and bstack1lll11ll1_opy_.bstack1l1llll1ll_opy_(bstack1111ll1111_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1l1l1lllll1_opy_(bstack1l1l111ll1l_opy_):
            bstack1lll11ll1_opy_.set_capabilities(bstack1111ll1111_opy_, CONFIG)
    if desired_capabilities:
        bstack11l1l11111_opy_ = bstack1l111ll111_opy_(desired_capabilities)
        bstack11l1l11111_opy_[bstack111l1l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ⑇")] = bstack1ll1l111l1_opy_(CONFIG)
        bstack1111l1ll11_opy_ = bstack1l11ll1l1l_opy_(bstack11l1l11111_opy_)
        if bstack1111l1ll11_opy_:
            bstack1111ll1111_opy_ = update(bstack1111l1ll11_opy_, bstack1111ll1111_opy_)
        desired_capabilities = None
    if options:
        bstack1ll1l11l1l_opy_(options, bstack1111ll1111_opy_)
    if not options:
        options = bstack1l1l1lll11_opy_(bstack1111ll1111_opy_)
    if proxy and bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭⑈")):
        options.proxy(proxy)
    if options and bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭⑉")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l11ll1lll_opy_() < version.parse(bstack111l1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ⑊")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1111ll1111_opy_)
    logger.info(bstack11l1l11l1l_opy_)
    bstack1l11l1l11_opy_.end(EVENTS.bstack111l1ll1ll_opy_.value, EVENTS.bstack111l1ll1ll_opy_.value + bstack111l1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ⑋"),
                               EVENTS.bstack111l1ll1ll_opy_.value + bstack111l1l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ⑌"), True, None)
    try:
        if bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ⑍")):
            bstack1l111ll1l_opy_(self, command_executor=command_executor,
                      options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
        elif bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ⑎")):
            bstack1l111ll1l_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities, options=options,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        elif bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭⑏")):
            bstack1l111ll1l_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        else:
            bstack1l111ll1l_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive)
    except Exception as bstack11lll1l111_opy_:
        logger.error(bstack1111l11l11_opy_.format(bstack111l1l_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰ࠭⑐"), str(bstack11lll1l111_opy_)))
        raise bstack11lll1l111_opy_
    try:
        bstack1111l1l111_opy_ = bstack111l1l_opy_ (u"ࠨࠩ⑑")
        if bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪ⑒")):
            bstack1111l1l111_opy_ = self.caps.get(bstack111l1l_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥ⑓"))
        else:
            bstack1111l1l111_opy_ = self.capabilities.get(bstack111l1l_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ⑔"))
        if bstack1111l1l111_opy_:
            bstack1l1111l111_opy_(bstack1111l1l111_opy_)
            if bstack1l11ll1lll_opy_() <= version.parse(bstack111l1l_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ⑕")):
                self.command_executor._url = bstack111l1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ⑖") + bstack1l111l11l1_opy_ + bstack111l1l_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦ⑗")
            else:
                self.command_executor._url = bstack111l1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ⑘") + bstack1111l1l111_opy_ + bstack111l1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥ⑙")
            logger.debug(bstack11ll1111ll_opy_.format(bstack1111l1l111_opy_))
        else:
            logger.debug(bstack1111l11lll_opy_.format(bstack111l1l_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦ⑚")))
    except Exception as e:
        logger.debug(bstack1111l11lll_opy_.format(e))
    bstack11lll11l1l_opy_ = self.session_id
    if bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ⑛") in bstack1lll1ll11l_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ⑜"), None)
        if item:
            bstack1lll1ll11l11_opy_ = getattr(item, bstack111l1l_opy_ (u"࠭࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࡢࡷࡹࡧࡲࡵࡧࡧࠫ⑝"), False)
            if not getattr(item, bstack111l1l_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ⑞"), None) and bstack1lll1ll11l11_opy_:
                setattr(store[bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ⑟")], bstack111l1l_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ①"), self)
        bstack111l1l1l1_opy_ = getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫ②"), None)
        if bstack111l1l1l1_opy_ and bstack111l1l1l1_opy_.get(bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ③"), bstack111l1l_opy_ (u"ࠬ࠭④")) == bstack111l1l_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ⑤"):
            bstack1l1l1111_opy_.bstack1l1l1111l1_opy_(self)
    bstack11llllll1_opy_.append(self)
    if bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⑥") in CONFIG and bstack111l1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⑦") in CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⑧")][bstack1l1lll11ll_opy_]:
        bstack111l111l1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭⑨")][bstack1l1lll11ll_opy_][bstack111l1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⑩")]
    logger.debug(bstack1l1ll1111l_opy_.format(bstack11lll11l1l_opy_))
@measure(event_name=EVENTS.bstack11l111ll11_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll1l1l1l_opy_(self, url):
    global bstack1ll1111lll_opy_
    global CONFIG
    try:
        bstack1l1l1lll1l_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack111l11l1ll_opy_.format(str(err)))
    try:
        bstack1ll1111lll_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack11111ll11_opy_):
                bstack1l1l1lll1l_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack111l11l1ll_opy_.format(str(err)))
        raise e
def bstack1ll111l11_opy_(item, when):
    global bstack111l111l11_opy_
    try:
        bstack111l111l11_opy_(item, when)
    except Exception as e:
        pass
def bstack111111ll1l_opy_(item, call, rep):
    global bstack1l11llllll_opy_
    global bstack11llllll1_opy_
    name = bstack111l1l_opy_ (u"ࠬ࠭⑪")
    try:
        if rep.when == bstack111l1l_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ⑫"):
            bstack11lll11l1l_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⑬"))
            try:
                if (str(skipSessionName).lower() != bstack111l1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭⑭")):
                    name = str(rep.nodeid)
                    bstack111lll1ll_opy_ = bstack1ll1l1l1ll_opy_(bstack111l1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⑮"), name, bstack111l1l_opy_ (u"ࠪࠫ⑯"), bstack111l1l_opy_ (u"ࠫࠬ⑰"), bstack111l1l_opy_ (u"ࠬ࠭⑱"), bstack111l1l_opy_ (u"࠭ࠧ⑲"))
                    os.environ[bstack111l1l_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪ⑳")] = name
                    for driver in bstack11llllll1_opy_:
                        if bstack11lll11l1l_opy_ == driver.session_id:
                            driver.execute_script(bstack111lll1ll_opy_)
            except Exception as e:
                logger.debug(bstack111l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ⑴").format(str(e)))
            try:
                bstack1llll11l1l_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ⑵"):
                    status = bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⑶") if rep.outcome.lower() == bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⑷") else bstack111l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ⑸")
                    reason = bstack111l1l_opy_ (u"࠭ࠧ⑹")
                    if status == bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⑺"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack111l1l_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭⑻") if status == bstack111l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⑼") else bstack111l1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ⑽")
                    data = name + bstack111l1l_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭⑾") if status == bstack111l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ⑿") else name + bstack111l1l_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠡࠡࠩ⒀") + reason
                    bstack11l11l1lll_opy_ = bstack1ll1l1l1ll_opy_(bstack111l1l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ⒁"), bstack111l1l_opy_ (u"ࠨࠩ⒂"), bstack111l1l_opy_ (u"ࠩࠪ⒃"), bstack111l1l_opy_ (u"ࠪࠫ⒄"), level, data)
                    for driver in bstack11llllll1_opy_:
                        if bstack11lll11l1l_opy_ == driver.session_id:
                            driver.execute_script(bstack11l11l1lll_opy_)
            except Exception as e:
                logger.debug(bstack111l1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡥࡲࡲࡹ࡫ࡸࡵࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ⒅").format(str(e)))
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡵࡷࡥࡹ࡫ࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻࡾࠩ⒆").format(str(e)))
    bstack1l11llllll_opy_(item, call, rep)
notset = Notset()
def bstack1l1l1111ll_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l1llll11l_opy_
    if str(name).lower() == bstack111l1l_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭⒇"):
        return bstack111l1l_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨ⒈")
    else:
        return bstack1l1llll11l_opy_(self, name, default, skip)
def bstack11ll1lll1_opy_(self):
    global CONFIG
    global bstack111l1ll1l1_opy_
    try:
        proxy = bstack111ll11ll_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack111l1l_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭⒉")):
                proxies = bstack1l11l1ll1_opy_(proxy, bstack1lll11llll_opy_())
                if len(proxies) > 0:
                    protocol, bstack11l11lllll_opy_ = proxies.popitem()
                    if bstack111l1l_opy_ (u"ࠤ࠽࠳࠴ࠨ⒊") in bstack11l11lllll_opy_:
                        return bstack11l11lllll_opy_
                    else:
                        return bstack111l1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ⒋") + bstack11l11lllll_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack111l1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣ⒌").format(str(e)))
    return bstack111l1ll1l1_opy_(self)
def bstack11l1l11ll1_opy_():
    return (bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ⒍") in CONFIG or bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ⒎") in CONFIG) and bstack1ll11l11l1_opy_() and bstack1l11ll1lll_opy_() >= version.parse(
        bstack1ll11ll1l1_opy_)
def bstack1111l1l1ll_opy_(self,
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
    global bstack111l111l1l_opy_
    global bstack1llllll1l1_opy_
    global bstack1lll1ll11l_opy_
    CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ⒏")] = str(bstack1lll1ll11l_opy_) + str(__version__)
    bstack1l1lll11ll_opy_ = 0
    try:
        if bstack1llllll1l1_opy_ is True:
            bstack1l1lll11ll_opy_ = int(os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ⒐")))
    except:
        bstack1l1lll11ll_opy_ = 0
    CONFIG[bstack111l1l_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ⒑")] = True
    bstack1111ll1111_opy_ = bstack1l11ll1l1l_opy_(CONFIG, bstack1l1lll11ll_opy_)
    logger.debug(bstack11l1llllll_opy_.format(str(bstack1111ll1111_opy_)))
    if CONFIG.get(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ⒒")):
        bstack1ll1l11ll_opy_(bstack1111ll1111_opy_, bstack1111l1111_opy_)
    if bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ⒓") in CONFIG and bstack111l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⒔") in CONFIG[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⒕")][bstack1l1lll11ll_opy_]:
        bstack111l111l1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⒖")][bstack1l1lll11ll_opy_][bstack111l1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⒗")]
    import urllib
    import json
    if bstack111l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⒘") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ⒙")]).lower() != bstack111l1l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ⒚"):
        bstack11l11l1l11_opy_ = bstack1111l1lll1_opy_()
        bstack111ll1l11_opy_ = bstack11l11l1l11_opy_ + urllib.parse.quote(json.dumps(bstack1111ll1111_opy_))
    else:
        bstack111ll1l11_opy_ = bstack111l1l_opy_ (u"ࠬࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠧ⒛") + urllib.parse.quote(json.dumps(bstack1111ll1111_opy_))
    browser = self.connect(bstack111ll1l11_opy_)
    return browser
def bstack1l111l11ll_opy_():
    global bstack11l1l1l11_opy_
    global bstack1lll1ll11l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111l11111_opy_
        if not bstack1lll1l1111l_opy_():
            global bstack11ll11l111_opy_
            if not bstack11ll11l111_opy_:
                from bstack_utils.helper import bstack11lll1llll_opy_, bstack11l1l1l111_opy_
                bstack11ll11l111_opy_ = bstack11lll1llll_opy_()
                bstack11l1l1l111_opy_(bstack1lll1ll11l_opy_)
            BrowserType.connect = bstack1111l11111_opy_
            return
        BrowserType.launch = bstack1111l1l1ll_opy_
        bstack11l1l1l11_opy_ = True
    except Exception as e:
        pass
def bstack1lll1lll11l1_opy_():
    global CONFIG
    global bstack11ll1l11ll_opy_
    global bstack1l111l11l1_opy_
    global bstack1111l1111_opy_
    global bstack1llllll1l1_opy_
    global bstack1ll1ll11l1_opy_
    CONFIG = json.loads(os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠬ⒜")))
    bstack11ll1l11ll_opy_ = eval(os.environ.get(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ⒝")))
    bstack1l111l11l1_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡉࡗࡅࡣ࡚ࡘࡌࠨ⒞"))
    bstack1ll111l11l_opy_(CONFIG, bstack11ll1l11ll_opy_)
    bstack1ll1ll11l1_opy_ = bstack1l11l1lll_opy_.configure_logger(CONFIG, bstack1ll1ll11l1_opy_)
    if cli.bstack11111l1lll_opy_():
        bstack111l1111l1_opy_.invoke(Events.CONNECT, bstack11l1l1l11l_opy_())
        cli_context.platform_index = int(os.environ.get(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ⒟"), bstack111l1l_opy_ (u"ࠪ࠴ࠬ⒠")))
        cli.bstack1l1l1ll11l1_opy_(cli_context.platform_index)
        cli.bstack1l11lll111l_opy_(bstack1lll11llll_opy_(bstack1l111l11l1_opy_, CONFIG), cli_context.platform_index, bstack1l1l1lll11_opy_)
        cli.bstack1l11lll11l1_opy_()
        logger.debug(bstack111l1l_opy_ (u"ࠦࡈࡒࡉࠡ࡫ࡶࠤࡦࡩࡴࡪࡸࡨࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࠥ⒡") + str(cli_context.platform_index) + bstack111l1l_opy_ (u"ࠧࠨ⒢"))
        return # skip all existing operations
    global bstack1l111ll1l_opy_
    global bstack11lllll1l1_opy_
    global bstack1ll11l1l1l_opy_
    global bstack1ll1lllll1_opy_
    global bstack1l1llllll_opy_
    global bstack11ll11lll1_opy_
    global bstack111lll11l1_opy_
    global bstack1ll1111lll_opy_
    global bstack111l1ll1l1_opy_
    global bstack1l1llll11l_opy_
    global bstack111l111l11_opy_
    global bstack1l11llllll_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1l111ll1l_opy_ = webdriver.Remote.__init__
        bstack11lllll1l1_opy_ = WebDriver.quit
        bstack111lll11l1_opy_ = WebDriver.close
        bstack1ll1111lll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ⒣") in CONFIG or bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ⒤") in CONFIG) and bstack1ll11l11l1_opy_():
        if bstack1l11ll1lll_opy_() < version.parse(bstack1ll11ll1l1_opy_):
            logger.error(bstack1l111lll1l_opy_.format(bstack1l11ll1lll_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack111l1l_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ⒥")) and callable(getattr(RemoteConnection, bstack111l1l_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ⒦"))):
                    bstack111l1ll1l1_opy_ = RemoteConnection._get_proxy_url
                else:
                    from selenium.webdriver.remote.client_config import ClientConfig
                    bstack111l1ll1l1_opy_ = ClientConfig.get_proxy_url
            except Exception as e:
                logger.error(bstack1ll1l1ll11_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1l1llll11l_opy_ = Config.getoption
        from _pytest import runner
        bstack111l111l11_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1lll1ll1l_opy_)
    try:
        from pytest_bdd import reporting
        bstack1l11llllll_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫ⒧"))
    bstack1111l1111_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ⒨"), {}).get(bstack111l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ⒩"))
    bstack1llllll1l1_opy_ = True
    bstack1l111llll_opy_(bstack1lll1l1ll1_opy_)
if (bstack111l1l111l1_opy_()):
    bstack1lll1lll11l1_opy_()
@error_handler(class_method=False)
def bstack1lll1ll1l11l_opy_(hook_name, event, bstack1ll1l1l1l1l_opy_=None):
    if hook_name not in [bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧ⒪"), bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫ⒫"), bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧ⒬"), bstack111l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫ⒭"), bstack111l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ⒮"), bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬ⒯"), bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫ⒰"), bstack111l1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨ⒱")]:
        return
    node = store[bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⒲")]
    if hook_name in [bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧ⒳"), bstack111l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫ⒴")]:
        node = store[bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡲࡵࡤࡶ࡮ࡨࡣ࡮ࡺࡥ࡮ࠩ⒵")]
    elif hook_name in [bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩⒶ"), bstack111l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭Ⓑ")]:
        node = store[bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡤ࡮ࡤࡷࡸࡥࡩࡵࡧࡰࠫⒸ")]
    hook_type = bstack11l111l1l11_opy_(hook_name)
    if event == bstack111l1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧⒹ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_[hook_type], bstack1llll111111_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack1llll1l1_opy_ = {
            bstack111l1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭Ⓔ"): uuid,
            bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ⓕ"): bstack1lllll11_opy_(),
            bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨⒼ"): bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩⒽ"),
            bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨⒾ"): hook_type,
            bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩⒿ"): hook_name
        }
        store[bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫⓀ")].append(uuid)
        bstack1lll1ll11l1l_opy_ = node.nodeid
        if hook_type == bstack111l1l_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭Ⓛ"):
            if not _1ll111ll_opy_.get(bstack1lll1ll11l1l_opy_, None):
                _1ll111ll_opy_[bstack1lll1ll11l1l_opy_] = {bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨⓂ"): []}
            _1ll111ll_opy_[bstack1lll1ll11l1l_opy_][bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩⓃ")].append(bstack1llll1l1_opy_[bstack111l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩⓄ")])
        _1ll111ll_opy_[bstack1lll1ll11l1l_opy_ + bstack111l1l_opy_ (u"ࠬ࠳ࠧⓅ") + hook_name] = bstack1llll1l1_opy_
        bstack1lll1lllllll_opy_(node, bstack1llll1l1_opy_, bstack111l1l_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧⓆ"))
    elif event == bstack111l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭Ⓡ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll11l1lll_opy_[hook_type], bstack1llll111111_opy_.POST, node, None, bstack1ll1l1l1l1l_opy_)
            return
        bstack1l11l1l1_opy_ = node.nodeid + bstack111l1l_opy_ (u"ࠨ࠯ࠪⓈ") + hook_name
        _1ll111ll_opy_[bstack1l11l1l1_opy_][bstack111l1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧⓉ")] = bstack1lllll11_opy_()
        bstack1lll1lllll11_opy_(_1ll111ll_opy_[bstack1l11l1l1_opy_][bstack111l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨⓊ")])
        bstack1lll1lllllll_opy_(node, _1ll111ll_opy_[bstack1l11l1l1_opy_], bstack111l1l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭Ⓥ"), bstack1lll1llll1l1_opy_=bstack1ll1l1l1l1l_opy_)
def bstack1lll1lll1l11_opy_():
    global bstack1lll1llll11l_opy_
    if bstack111ll1llll_opy_():
        bstack1lll1llll11l_opy_ = bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩⓌ")
    else:
        bstack1lll1llll11l_opy_ = bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭Ⓧ")
@bstack1l1l1111_opy_.bstack1llll11llll1_opy_
def bstack1lll1lllll1l_opy_():
    bstack1lll1lll1l11_opy_()
    if cli.is_running():
        try:
            bstack11l1l1llll1_opy_(bstack1lll1ll1l11l_opy_)
        except Exception as e:
            logger.debug(bstack111l1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࡷࠥࡶࡡࡵࡥ࡫࠾ࠥࢁࡽࠣⓎ").format(e))
        return
    if bstack1ll11l11l1_opy_():
        bstack1lllll1l1_opy_ = Config.bstack1111ll1l_opy_()
        bstack111l1l_opy_ (u"ࠨࠩࠪࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡉࡳࡷࠦࡰࡱࡲࠣࡁࠥ࠷ࠬࠡ࡯ࡲࡨࡤ࡫ࡸࡦࡥࡸࡸࡪࠦࡧࡦࡶࡶࠤࡺࡹࡥࡥࠢࡩࡳࡷࠦࡡ࠲࠳ࡼࠤࡨࡵ࡭࡮ࡣࡱࡨࡸ࠳ࡷࡳࡣࡳࡴ࡮ࡴࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡆࡰࡴࠣࡴࡵࡶࠠ࠿ࠢ࠴࠰ࠥࡳ࡯ࡥࡡࡨࡼࡪࡩࡵࡵࡧࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡥࡩࡨࡧࡵࡴࡧࠣ࡭ࡹࠦࡩࡴࠢࡳࡥࡹࡩࡨࡦࡦࠣ࡭ࡳࠦࡡࠡࡦ࡬ࡪ࡫࡫ࡲࡦࡰࡷࠤࡵࡸ࡯ࡤࡧࡶࡷࠥ࡯ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩࡷࡶࠤࡼ࡫ࠠ࡯ࡧࡨࡨࠥࡺ࡯ࠡࡷࡶࡩ࡙ࠥࡥ࡭ࡧࡱ࡭ࡺࡳࡐࡢࡶࡦ࡬࠭ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡩࡣࡱࡨࡱ࡫ࡲࠪࠢࡩࡳࡷࠦࡰࡱࡲࠣࡂࠥ࠷ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩࠪࠫⓏ")
        if bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭ⓐ")):
            if CONFIG.get(bstack111l1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪⓑ")) is not None and int(CONFIG[bstack111l1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫⓒ")]) > 1:
                bstack1ll1ll1l1l_opy_(bstack1ll1ll1l11_opy_)
            return
        bstack1ll1ll1l1l_opy_(bstack1ll1ll1l11_opy_)
    try:
        bstack11l1l1llll1_opy_(bstack1lll1ll1l11l_opy_)
    except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࡵࠣࡴࡦࡺࡣࡩ࠼ࠣࡿࢂࠨⓓ").format(e))
bstack1lll1lllll1l_opy_()