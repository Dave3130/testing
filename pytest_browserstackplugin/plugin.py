# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack111l1111l_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11111lll1_opy_, bstack11lllll11_opy_, update, bstack1l1l11l111_opy_,
                                       bstack1l11111l1l_opy_, bstack1l1ll1ll1l_opy_, bstack1ll1l1lll_opy_, bstack11l1111ll_opy_,
                                       bstack1lll11l1l1_opy_, bstack1l1ll11ll1_opy_, bstack111111l1l1_opy_,
                                       bstack1111111ll_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack11l1111l1_opy_)
from browserstack_sdk.bstack11111111_opy_ import bstack111ll11l_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack11llll111l_opy_
from bstack_utils.capture import bstack1l1l1lll_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack1l11llll1_opy_, bstack1l1l1l1lll_opy_, bstack11ll11l1l1_opy_, \
    bstack1l11111lll_opy_
from bstack_utils.helper import bstack1l11l1l1_opy_, bstack1111l111lll_opy_, bstack1l111ll1_opy_, bstack111ll1111l_opy_, bstack1lll1ll11ll_opy_, bstack1l1111ll_opy_, \
    bstack1111l11l1l1_opy_, \
    bstack111l1l1l1l1_opy_, bstack1l111llll1_opy_, bstack11l1l11lll_opy_, bstack111l1111ll1_opy_, bstack11l1ll11l1_opy_, Notset, \
    bstack111ll1l11_opy_, bstack111l11ll1l1_opy_, bstack1111lll11l1_opy_, Result, bstack1111ll1llll_opy_, bstack111l111l1l1_opy_, error_handler, \
    bstack1l11ll111l_opy_, bstack111ll1lll_opy_, bstack1111l11l1l_opy_, bstack111l1ll1111_opy_
from bstack_utils.bstack11l1l1l1ll1_opy_ import bstack11l1l1lllll_opy_
from bstack_utils.messages import bstack1ll11ll11l_opy_, bstack111l111l1_opy_, bstack1111l11l1_opy_, bstack11l1l1l1ll_opy_, bstack1111l111_opy_, \
    bstack11lll11l1_opy_, bstack1lllllll11_opy_, bstack11l1lll11l_opy_, bstack111lll1ll1_opy_, bstack111l1l1ll1_opy_, \
    bstack1llll1ll11_opy_, bstack111l1lll1_opy_, bstack11lll1ll1_opy_
from bstack_utils.proxy import bstack111l11ll1_opy_, bstack11l1111lll_opy_
from bstack_utils.bstack1l11ll1lll_opy_ import bstack11l111ll11l_opy_, bstack11l111l1ll1_opy_, bstack11l111l1l11_opy_, bstack11l111ll1l1_opy_, \
    bstack11l111l111l_opy_, bstack11l111lll11_opy_, bstack11l111l11l1_opy_, bstack11ll11llll_opy_, bstack11l111l11ll_opy_
from bstack_utils.bstack1l1l111lll_opy_ import bstack11ll1ll11_opy_
from bstack_utils.bstack1l1ll111l1_opy_ import bstack111lll1l11_opy_, bstack1l11l1111_opy_, bstack1llll1l1l1_opy_, \
    bstack1l1ll1l11_opy_, bstack1l1ll111ll_opy_
from bstack_utils.bstack11lll1ll_opy_ import bstack1lllll11_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack1ll11l1l_opy_
import bstack_utils.accessibility as bstack1111ll1l_opy_
from bstack_utils.bstack1l1ll111_opy_ import bstack1ll1l1l1_opy_
from bstack_utils.bstack11l11l11ll_opy_ import bstack11l11l11ll_opy_
from bstack_utils.bstack111l1l1l_opy_ import bstack111l11ll_opy_
from browserstack_sdk.__init__ import bstack1l1ll1lll1_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1l111l1_opy_ import bstack1l1l111llll_opy_
from browserstack_sdk.sdk_cli.bstack1l11l1lll_opy_ import bstack1l11l1lll_opy_, Events, bstack111lllllll_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1ll11l11l11_opy_, bstack1llll111l1l_opy_, bstack1lll1lll111_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l11l1lll_opy_ import bstack1l11l1lll_opy_, Events, bstack111lllllll_opy_
bstack1l11ll1ll1_opy_ = None
bstack1lll1l1lll_opy_ = None
bstack11l1l1llll_opy_ = None
bstack1ll11l11l_opy_ = None
bstack1llll1l1ll_opy_ = None
bstack1l1ll1lll_opy_ = None
bstack1lll1ll111_opy_ = None
bstack1111l11lll_opy_ = None
bstack1ll1ll1l11_opy_ = None
bstack11l11l1lll_opy_ = None
bstack11111l1lll_opy_ = None
bstack1lllllllll_opy_ = None
bstack11111l11l1_opy_ = None
bstack1l11ll11l1_opy_ = bstack1lllll1l_opy_ (u"ࠨࠩ≵")
CONFIG = {}
bstack1l1111l11l_opy_ = False
bstack11lll1111_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪ≶")
bstack1l1l1l111_opy_ = bstack1lllll1l_opy_ (u"ࠪࠫ≷")
bstack11l11l1ll1_opy_ = False
bstack1111lll11l_opy_ = []
bstack111l1ll11_opy_ = bstack1l11llll1_opy_
bstack1lll1ll1l111_opy_ = bstack1lllll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ≸")
bstack1lll111111_opy_ = {}
bstack1l1ll1l1l1_opy_ = None
bstack1ll1ll1111_opy_ = False
logger = bstack11llll111l_opy_.get_logger(__name__, bstack111l1ll11_opy_)
store = {
    bstack1lllll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ≹"): []
}
bstack1lll1ll1ll1l_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1ll1l111_opy_ = {}
current_test_uuid = None
cli_context = bstack1ll11l11l11_opy_(
    test_framework_name=bstack1l1111l11_opy_[bstack1lllll1l_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪ≺")] if bstack11l1ll11l1_opy_() else bstack1l1111l11_opy_[bstack1lllll1l_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚ࠧ≻")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack111111l1l_opy_(page, bstack1ll11l1l1l_opy_):
    try:
        page.evaluate(bstack1lllll1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ≼"),
                      bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭≽") + json.dumps(
                          bstack1ll11l1l1l_opy_) + bstack1lllll1l_opy_ (u"ࠥࢁࢂࠨ≾"))
    except Exception as e:
        print(bstack1lllll1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤ≿"), e)
def bstack1l111lll1_opy_(page, message, level):
    try:
        page.evaluate(bstack1lllll1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ⊀"), bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ⊁") + json.dumps(
            message) + bstack1lllll1l_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪ⊂") + json.dumps(level) + bstack1lllll1l_opy_ (u"ࠨࡿࢀࠫ⊃"))
    except Exception as e:
        print(bstack1lllll1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧ⊄"), e)
def pytest_configure(config):
    global bstack11lll1111_opy_
    global CONFIG
    bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
    config.args = bstack1ll11l1l_opy_.bstack11l11l111ll_opy_(config.args)
    bstack1lll1ll1l_opy_.bstack11ll11lll1_opy_(bstack1111l11l1l_opy_(config.getoption(bstack1lllll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ⊅"))))
    try:
        bstack11llll111l_opy_.bstack11111l1llll_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack1l11l1lll_opy_.invoke(Events.CONNECT, bstack111lllllll_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ⊆"), bstack1lllll1l_opy_ (u"ࠬ࠶ࠧ⊇")))
        config = json.loads(os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠧ⊈"), bstack1lllll1l_opy_ (u"ࠢࡼࡿࠥ⊉")))
        cli.bstack1l1l1l1ll1l_opy_(bstack11l1l11lll_opy_(bstack11lll1111_opy_, CONFIG), cli_context.platform_index, bstack1l1l11l111_opy_)
    if cli.bstack1l11llll1l1_opy_(bstack1l1l111llll_opy_):
        cli.bstack1l1l1111l1l_opy_()
        logger.debug(bstack1lllll1l_opy_ (u"ࠣࡅࡏࡍࠥ࡯ࡳࠡࡣࡦࡸ࡮ࡼࡥࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢ⊊") + str(cli_context.platform_index) + bstack1lllll1l_opy_ (u"ࠤࠥ⊋"))
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.BEFORE_ALL, bstack1lll1lll111_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack1lllll1l_opy_ (u"ࠥࡻ࡭࡫࡮ࠣ⊌"), None)
    if cli.is_running() and when == bstack1lllll1l_opy_ (u"ࠦࡨࡧ࡬࡭ࠤ⊍"):
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.LOG_REPORT, bstack1lll1lll111_opy_.PRE, item, call)
    outcome = yield
    if when == bstack1lllll1l_opy_ (u"ࠧࡩࡡ࡭࡮ࠥ⊎"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1lllll1l_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣ⊏")))
        if not passed:
            config = json.loads(os.environ.get(bstack1lllll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࠨ⊐"), bstack1lllll1l_opy_ (u"ࠣࡽࢀࠦ⊑")))
            if bstack111l11ll_opy_.bstack1111lll1_opy_(config):
                bstack1111111111l_opy_ = bstack111l11ll_opy_.bstack1llllllll_opy_(config)
                if item.execution_count > bstack1111111111l_opy_:
                    print(bstack1lllll1l_opy_ (u"ࠩࡗࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡲࡦࡶࡵ࡭ࡪࡹ࠺ࠡࠩ⊒"), report.nodeid, os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ⊓")))
                    bstack111l11ll_opy_.bstack111ll1lllll_opy_(report.nodeid)
            else:
                print(bstack1lllll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࠫ⊔"), report.nodeid, os.environ.get(bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ⊕")))
                bstack111l11ll_opy_.bstack111ll1lllll_opy_(report.nodeid)
        else:
            print(bstack1lllll1l_opy_ (u"࠭ࡔࡦࡵࡷࠤࡵࡧࡳࡴࡧࡧ࠾ࠥ࠭⊖"), report.nodeid, os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⊗")))
    if cli.is_running():
        if when == bstack1lllll1l_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢ⊘"):
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.BEFORE_EACH, bstack1lll1lll111_opy_.POST, item, call, outcome)
        elif when == bstack1lllll1l_opy_ (u"ࠤࡦࡥࡱࡲࠢ⊙"):
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.LOG_REPORT, bstack1lll1lll111_opy_.POST, item, call, outcome)
        elif when == bstack1lllll1l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧ⊚"):
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.AFTER_EACH, bstack1lll1lll111_opy_.POST, item, call, outcome)
        return # skip all existing operations
    skipSessionName = item.config.getoption(bstack1lllll1l_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⊛"))
    plugins = item.config.getoption(bstack1lllll1l_opy_ (u"ࠧࡶ࡬ࡶࡩ࡬ࡲࡸࠨ⊜"))
    report = outcome.get_result()
    os.environ[bstack1lllll1l_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ⊝")] = report.nodeid
    bstack1lll1ll1ll11_opy_(item, call, report)
    if bstack1lllll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡶ࡬ࡶࡩ࡬ࡲࠧ⊞") not in plugins or bstack11l1ll11l1_opy_():
        return
    summary = []
    driver = getattr(item, bstack1lllll1l_opy_ (u"ࠣࡡࡧࡶ࡮ࡼࡥࡳࠤ⊟"), None)
    page = getattr(item, bstack1lllll1l_opy_ (u"ࠤࡢࡴࡦ࡭ࡥࠣ⊠"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1lll1ll1l1l1_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1lll1ll11ll1_opy_(item, report, summary, skipSessionName)
def bstack1lll1ll1l1l1_opy_(item, report, summary, skipSessionName):
    if report.when == bstack1lllll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ⊡") and report.skipped:
        bstack11l111l11ll_opy_(report)
    if report.when in [bstack1lllll1l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥ⊢"), bstack1lllll1l_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢ⊣")]:
        return
    if not bstack1lll1ll11ll_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack1lllll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫ⊤")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬ⊥") + json.dumps(
                    report.nodeid) + bstack1lllll1l_opy_ (u"ࠨࡿࢀࠫ⊦"))
        os.environ[bstack1lllll1l_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬ⊧")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack1lllll1l_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩ࠿ࠦࡻ࠱ࡿࠥ⊨").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1lllll1l_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨ⊩")))
    bstack11lll11111_opy_ = bstack1lllll1l_opy_ (u"ࠧࠨ⊪")
    bstack11l111l11ll_opy_(report)
    if not passed:
        try:
            bstack11lll11111_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack1lllll1l_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨ⊫").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack11lll11111_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack1lllll1l_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤ⊬")))
        bstack11lll11111_opy_ = bstack1lllll1l_opy_ (u"ࠣࠤ⊭")
        if not passed:
            try:
                bstack11lll11111_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1lllll1l_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤ⊮").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack11lll11111_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡤࡢࡶࡤࠦ࠿ࠦࠧ⊯")
                    + json.dumps(bstack1lllll1l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠥࠧ⊰"))
                    + bstack1lllll1l_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣ⊱")
                )
            else:
                item._driver.execute_script(
                    bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫ⊲")
                    + json.dumps(str(bstack11lll11111_opy_))
                    + bstack1lllll1l_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥ⊳")
                )
        except Exception as e:
            summary.append(bstack1lllll1l_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡡ࡯ࡰࡲࡸࡦࡺࡥ࠻ࠢࡾ࠴ࢂࠨ⊴").format(e))
def bstack1lll1ll1llll_opy_(test_name, error_message):
    try:
        bstack1lll1lllllll_opy_ = []
        bstack11ll1l1ll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ⊵"), bstack1lllll1l_opy_ (u"ࠪ࠴ࠬ⊶"))
        bstack1l1ll11l1l_opy_ = {bstack1lllll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⊷"): test_name, bstack1lllll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ⊸"): error_message, bstack1lllll1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ⊹"): bstack11ll1l1ll_opy_}
        bstack1llll1111111_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ⊺"))
        if os.path.exists(bstack1llll1111111_opy_):
            with open(bstack1llll1111111_opy_) as f:
                bstack1lll1lllllll_opy_ = json.load(f)
        bstack1lll1lllllll_opy_.append(bstack1l1ll11l1l_opy_)
        with open(bstack1llll1111111_opy_, bstack1lllll1l_opy_ (u"ࠨࡹࠪ⊻")) as f:
            json.dump(bstack1lll1lllllll_opy_, f)
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵ࡫ࡲࡴ࡫ࡶࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡶࡹࡵࡧࡶࡸࠥ࡫ࡲࡳࡱࡵࡷ࠿ࠦࠧ⊼") + str(e))
def bstack1lll1ll11ll1_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack1lllll1l_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤ⊽"), bstack1lllll1l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ⊾")]:
        return
    if (str(skipSessionName).lower() != bstack1lllll1l_opy_ (u"ࠬࡺࡲࡶࡧࠪ⊿")):
        bstack111111l1l_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1lllll1l_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣ⋀")))
    bstack11lll11111_opy_ = bstack1lllll1l_opy_ (u"ࠢࠣ⋁")
    bstack11l111l11ll_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack11lll11111_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1lllll1l_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣ⋂").format(e)
                )
        try:
            if passed:
                bstack1l1ll111ll_opy_(getattr(item, bstack1lllll1l_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨ⋃"), None), bstack1lllll1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ⋄"))
            else:
                error_message = bstack1lllll1l_opy_ (u"ࠫࠬ⋅")
                if bstack11lll11111_opy_:
                    bstack1l111lll1_opy_(item._page, str(bstack11lll11111_opy_), bstack1lllll1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ⋆"))
                    bstack1l1ll111ll_opy_(getattr(item, bstack1lllll1l_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬ⋇"), None), bstack1lllll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ⋈"), str(bstack11lll11111_opy_))
                    error_message = str(bstack11lll11111_opy_)
                else:
                    bstack1l1ll111ll_opy_(getattr(item, bstack1lllll1l_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧ⋉"), None), bstack1lllll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ⋊"))
                bstack1lll1ll1llll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack1lllll1l_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿ࠵ࢃࠢ⋋").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack1lllll1l_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ⋌"), default=bstack1lllll1l_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦ⋍"), help=bstack1lllll1l_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧ⋎"))
    parser.addoption(bstack1lllll1l_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨ⋏"), default=bstack1lllll1l_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢ⋐"), help=bstack1lllll1l_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣ⋑"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack1lllll1l_opy_ (u"ࠥ࠱࠲ࡪࡲࡪࡸࡨࡶࠧ⋒"), action=bstack1lllll1l_opy_ (u"ࠦࡸࡺ࡯ࡳࡧࠥ⋓"), default=bstack1lllll1l_opy_ (u"ࠧࡩࡨࡳࡱࡰࡩࠧ⋔"),
                         help=bstack1lllll1l_opy_ (u"ࠨࡄࡳ࡫ࡹࡩࡷࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷࠧ⋕"))
def bstack1llll1ll_opy_(log):
    if not (log[bstack1lllll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⋖")] and log[bstack1lllll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⋗")].strip()):
        return
    active = bstack1ll1ll1l_opy_()
    log = {
        bstack1lllll1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⋘"): log[bstack1lllll1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ⋙")],
        bstack1lllll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⋚"): bstack1l111ll1_opy_().isoformat() + bstack1lllll1l_opy_ (u"ࠬࡠࠧ⋛"),
        bstack1lllll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⋜"): log[bstack1lllll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⋝")],
    }
    if active:
        if active[bstack1lllll1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭⋞")] == bstack1lllll1l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⋟"):
            log[bstack1lllll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⋠")] = active[bstack1lllll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⋡")]
        elif active[bstack1lllll1l_opy_ (u"ࠬࡺࡹࡱࡧࠪ⋢")] == bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࠫ⋣"):
            log[bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⋤")] = active[bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⋥")]
    bstack1ll1l1l1_opy_.bstack1ll1llll_opy_([log])
def bstack1ll1ll1l_opy_():
    if len(store[bstack1lllll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⋦")]) > 0 and store[bstack1lllll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ⋧")][-1]:
        return {
            bstack1lllll1l_opy_ (u"ࠫࡹࡿࡰࡦࠩ⋨"): bstack1lllll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⋩"),
            bstack1lllll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⋪"): store[bstack1lllll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⋫")][-1]
        }
    if store.get(bstack1lllll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⋬"), None):
        return {
            bstack1lllll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⋭"): bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࠨ⋮"),
            bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⋯"): store[bstack1lllll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ⋰")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.INIT_TEST, bstack1lll1lll111_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.INIT_TEST, bstack1lll1lll111_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1llll111111l_opy_ = True
        bstack111l11111l_opy_ = bstack1111ll1l_opy_.bstack1ll1l11ll_opy_(bstack111l1l1l1l1_opy_(item.own_markers))
        if not cli.bstack1l11llll1l1_opy_(bstack1l1l111llll_opy_):
            item._a11y_test_case = bstack111l11111l_opy_
            if bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ⋱"), None):
                driver = getattr(item, bstack1lllll1l_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ⋲"), None)
                item._a11y_started = bstack1111ll1l_opy_.bstack1ll1lll1l_opy_(driver, bstack111l11111l_opy_)
        if not bstack1ll1l1l1_opy_.on() or bstack1lll1ll1l111_opy_ != bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ⋳"):
            return
        global current_test_uuid #, bstack1l11111l_opy_
        bstack1ll1lll1_opy_ = {
            bstack1lllll1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⋴"): uuid4().__str__(),
            bstack1lllll1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⋵"): bstack1l111ll1_opy_().isoformat() + bstack1lllll1l_opy_ (u"ࠫ࡟࠭⋶")
        }
        current_test_uuid = bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪ⋷")]
        store[bstack1lllll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ⋸")] = bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⋹")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1ll1l111_opy_[item.nodeid] = {**_1ll1l111_opy_[item.nodeid], **bstack1ll1lll1_opy_}
        bstack1lll1lll11l1_opy_(item, _1ll1l111_opy_[item.nodeid], bstack1lllll1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⋺"))
    except Exception as err:
        print(bstack1lllll1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡦࡥࡱࡲ࠺ࠡࡽࢀࠫ⋻"), str(err))
def pytest_runtest_setup(item):
    store[bstack1lllll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ⋼")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.BEFORE_EACH, bstack1lll1lll111_opy_.PRE, item, bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ⋽"))
    if bstack111l11ll_opy_.bstack111llll11ll_opy_():
            bstack1lll1ll111ll_opy_ = bstack1lllll1l_opy_ (u"࡙ࠧ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡧࡳࠡࡶ࡫ࡩࠥࡧࡢࡰࡴࡷࠤࡧࡻࡩ࡭ࡦࠣࡪ࡮ࡲࡥࠡࡧࡻ࡭ࡸࡺࡳ࠯ࠤ⋾")
            logger.error(bstack1lll1ll111ll_opy_)
            bstack1ll1lll1_opy_ = {
                bstack1lllll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⋿"): uuid4().__str__(),
                bstack1lllll1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⌀"): bstack1l111ll1_opy_().isoformat() + bstack1lllll1l_opy_ (u"ࠨ࡜ࠪ⌁"),
                bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⌂"): bstack1l111ll1_opy_().isoformat() + bstack1lllll1l_opy_ (u"ࠪ࡞ࠬ⌃"),
                bstack1lllll1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⌄"): bstack1lllll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭⌅"),
                bstack1lllll1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭⌆"): bstack1lll1ll111ll_opy_,
                bstack1lllll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⌇"): [],
                bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ⌈"): []
            }
            bstack1lll1lll11l1_opy_(item, bstack1ll1lll1_opy_, bstack1lllll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪ⌉"))
            pytest.skip(bstack1lll1ll111ll_opy_)
            return # skip all existing operations
    global bstack1lll1ll1ll1l_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111l1111ll1_opy_():
        atexit.register(bstack11l11111l_opy_)
        if not bstack1lll1ll1ll1l_opy_:
            try:
                bstack1lll1lllll1l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack111l1ll1111_opy_():
                    bstack1lll1lllll1l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1lllll1l_opy_:
                    signal.signal(s, bstack1lll1llllll1_opy_)
                bstack1lll1ll1ll1l_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack1lllll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡨ࡫ࡶࡸࡪࡸࠠࡴ࡫ࡪࡲࡦࡲࠠࡩࡣࡱࡨࡱ࡫ࡲࡴ࠼ࠣࠦ⌊") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l111ll11l_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack1lllll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ⌋")
    try:
        if not bstack1ll1l1l1_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack1ll1lll1_opy_ = {
            bstack1lllll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪ⌌"): uuid,
            bstack1lllll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⌍"): bstack1l111ll1_opy_().isoformat() + bstack1lllll1l_opy_ (u"࡛ࠧࠩ⌎"),
            bstack1lllll1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭⌏"): bstack1lllll1l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⌐"),
            bstack1lllll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭⌑"): bstack1lllll1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩ⌒"),
            bstack1lllll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨ⌓"): bstack1lllll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ⌔")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack1lllll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⌕")] = item
        store[bstack1lllll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⌖")] = [uuid]
        if not _1ll1l111_opy_.get(item.nodeid, None):
            _1ll1l111_opy_[item.nodeid] = {bstack1lllll1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⌗"): [], bstack1lllll1l_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ⌘"): []}
        _1ll1l111_opy_[item.nodeid][bstack1lllll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⌙")].append(bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪ⌚")])
        _1ll1l111_opy_[item.nodeid + bstack1lllll1l_opy_ (u"࠭࠭ࡴࡧࡷࡹࡵ࠭⌛")] = bstack1ll1lll1_opy_
        bstack1lll1lll111l_opy_(item, bstack1ll1lll1_opy_, bstack1lllll1l_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ⌜"))
    except Exception as err:
        print(bstack1lllll1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡳࡷࡱࡸࡪࡹࡴࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫ⌝"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.AFTER_EACH, bstack1lll1lll111_opy_.PRE, item, bstack1lllll1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫ⌞"))
        return # skip all existing operations
    try:
        global bstack1lll111111_opy_
        bstack11ll1l1ll_opy_ = 0
        if bstack11l11l1ll1_opy_ is True:
            bstack11ll1l1ll_opy_ = int(os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ⌟")))
        if bstack11111lll1l_opy_.bstack1lllll11l1_opy_() == bstack1lllll1l_opy_ (u"ࠦࡹࡸࡵࡦࠤ⌠"):
            if bstack11111lll1l_opy_.bstack1ll11l111_opy_() == bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢ⌡"):
                bstack1lll1ll11lll_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⌢"), None)
                bstack1l1ll1ll1_opy_ = bstack1lll1ll11lll_opy_ + bstack1lllll1l_opy_ (u"ࠢ࠮ࡶࡨࡷࡹࡩࡡࡴࡧࠥ⌣")
                driver = getattr(item, bstack1lllll1l_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ⌤"), None)
                bstack1l1l1l1l1_opy_ = getattr(item, bstack1lllll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ⌥"), None)
                bstack11l1llllll_opy_ = getattr(item, bstack1lllll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⌦"), None)
                PercySDK.screenshot(driver, bstack1l1ll1ll1_opy_, bstack1l1l1l1l1_opy_=bstack1l1l1l1l1_opy_, bstack11l1llllll_opy_=bstack11l1llllll_opy_, bstack1l11111111_opy_=bstack11ll1l1ll_opy_)
        if not cli.bstack1l11llll1l1_opy_(bstack1l1l111llll_opy_):
            if getattr(item, bstack1lllll1l_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡧࡲࡵࡧࡧࠫ⌧"), False):
                bstack111ll11l_opy_.bstack111l111l_opy_(getattr(item, bstack1lllll1l_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭⌨"), None), bstack1lll111111_opy_, logger, item)
        if not bstack1ll1l1l1_opy_.on():
            return
        bstack1ll1lll1_opy_ = {
            bstack1lllll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ〈"): uuid4().__str__(),
            bstack1lllll1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ〉"): bstack1l111ll1_opy_().isoformat() + bstack1lllll1l_opy_ (u"ࠨ࡜ࠪ⌫"),
            bstack1lllll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⌬"): bstack1lllll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ⌭"),
            bstack1lllll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ⌮"): bstack1lllll1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩ⌯"),
            bstack1lllll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ⌰"): bstack1lllll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ⌱")
        }
        _1ll1l111_opy_[item.nodeid + bstack1lllll1l_opy_ (u"ࠨ࠯ࡷࡩࡦࡸࡤࡰࡹࡱࠫ⌲")] = bstack1ll1lll1_opy_
        bstack1lll1lll111l_opy_(item, bstack1ll1lll1_opy_, bstack1lllll1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⌳"))
    except Exception as err:
        print(bstack1lllll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲ࠿ࠦࡻࡾࠩ⌴"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l111ll1l1_opy_(fixturedef.argname):
        store[bstack1lllll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡯ࡴࡦ࡯ࠪ⌵")] = request.node
    elif bstack11l111l111l_opy_(fixturedef.argname):
        store[bstack1lllll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪ⌶")] = request.node
    if not bstack1ll1l1l1_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.SETUP_FIXTURE, bstack1lll1lll111_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.SETUP_FIXTURE, bstack1lll1lll111_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.SETUP_FIXTURE, bstack1lll1lll111_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.SETUP_FIXTURE, bstack1lll1lll111_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    try:
        fixture = {
            bstack1lllll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⌷"): fixturedef.argname,
            bstack1lllll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⌸"): bstack1111l11l1l1_opy_(outcome),
            bstack1lllll1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪ⌹"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack1lllll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭⌺")]
        if not _1ll1l111_opy_.get(current_test_item.nodeid, None):
            _1ll1l111_opy_[current_test_item.nodeid] = {bstack1lllll1l_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ⌻"): []}
        _1ll1l111_opy_[current_test_item.nodeid][bstack1lllll1l_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭⌼")].append(fixture)
    except Exception as err:
        logger.debug(bstack1lllll1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨ⌽"), str(err))
if bstack11l1ll11l1_opy_() and bstack1ll1l1l1_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.STEP, bstack1lll1lll111_opy_.PRE, request, step)
            return
        try:
            _1ll1l111_opy_[request.node.nodeid][bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ⌾")].bstack111lllll_opy_(id(step))
        except Exception as err:
            print(bstack1lllll1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬ⌿"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.STEP, bstack1lll1lll111_opy_.POST, request, step, exception)
            return
        try:
            _1ll1l111_opy_[request.node.nodeid][bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ⍀")].bstack1lll1ll1_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack1lllll1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡹࡴࡦࡲࡢࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂ࠭⍁"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.STEP, bstack1lll1lll111_opy_.POST, request, step)
            return
        try:
            bstack11lll1ll_opy_: bstack1lllll11_opy_ = _1ll1l111_opy_[request.node.nodeid][bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⍂")]
            bstack11lll1ll_opy_.bstack1lll1ll1_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack1lllll1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡴࡶࡨࡴࡤ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠨ⍃"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1ll1l111_opy_
        try:
            if not bstack1ll1l1l1_opy_.on() or bstack1lll1ll1l111_opy_ != bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩ⍄"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ⍅"), None)
            if not _1ll1l111_opy_.get(request.node.nodeid, None):
                _1ll1l111_opy_[request.node.nodeid] = {}
            bstack11lll1ll_opy_ = bstack1lllll11_opy_.bstack111111l1l11_opy_(
                scenario, feature, request.node,
                name=bstack11l111lll11_opy_(request.node, scenario),
                started_at=bstack1l1111ll_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack1lllll1l_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩ⍆"),
                tags=bstack11l111l11l1_opy_(feature, scenario),
                bstack11lll111_opy_=bstack1ll1l1l1_opy_.bstack1ll111l1_opy_(driver) if driver and driver.session_id else {}
            )
            _1ll1l111_opy_[request.node.nodeid][bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ⍇")] = bstack11lll1ll_opy_
            bstack1lll1lllll11_opy_(bstack11lll1ll_opy_.uuid)
            bstack1ll1l1l1_opy_.bstack1lll11ll_opy_(bstack1lllll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⍈"), bstack11lll1ll_opy_)
        except Exception as err:
            print(bstack1lllll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬ⍉"), str(err))
def bstack1lll1lll1111_opy_(bstack11l11lll_opy_):
    if bstack11l11lll_opy_ in store[bstack1lllll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⍊")]:
        store[bstack1lllll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⍋")].remove(bstack11l11lll_opy_)
def bstack1lll1lllll11_opy_(test_uuid):
    store[bstack1lllll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ⍌")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1ll1l1l1_opy_.bstack1llll11l1ll1_opy_
def bstack1lll1ll1ll11_opy_(item, call, report):
    logger.debug(bstack1lllll1l_opy_ (u"ࠧࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡷࡹࡧࡲࡵࠩ⍍"))
    global bstack1lll1ll1l111_opy_
    bstack11lllllll_opy_ = bstack1l1111ll_opy_()
    if hasattr(report, bstack1lllll1l_opy_ (u"ࠨࡵࡷࡳࡵ࠭⍎")):
        bstack11lllllll_opy_ = bstack1111ll1llll_opy_(report.stop)
    elif hasattr(report, bstack1lllll1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࠨ⍏")):
        bstack11lllllll_opy_ = bstack1111ll1llll_opy_(report.start)
    try:
        if getattr(report, bstack1lllll1l_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⍐"), bstack1lllll1l_opy_ (u"ࠫࠬ⍑")) == bstack1lllll1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ⍒"):
            logger.debug(bstack1lllll1l_opy_ (u"࠭ࡨࡢࡰࡧࡰࡪࡥ࡯࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡶࡸࡦࡺࡥࠡ࠯ࠣࡿࢂ࠲ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࠱ࠥࢁࡽࠨ⍓").format(getattr(report, bstack1lllll1l_opy_ (u"ࠧࡸࡪࡨࡲࠬ⍔"), bstack1lllll1l_opy_ (u"ࠨࠩ⍕")).__str__(), bstack1lll1ll1l111_opy_))
            if bstack1lll1ll1l111_opy_ == bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ⍖"):
                _1ll1l111_opy_[item.nodeid][bstack1lllll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⍗")] = bstack11lllllll_opy_
                bstack1lll1lll11l1_opy_(item, _1ll1l111_opy_[item.nodeid], bstack1lllll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭⍘"), report, call)
                store[bstack1lllll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ⍙")] = None
            elif bstack1lll1ll1l111_opy_ == bstack1lllll1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥ⍚"):
                bstack11lll1ll_opy_ = _1ll1l111_opy_[item.nodeid][bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ⍛")]
                bstack11lll1ll_opy_.set(hooks=_1ll1l111_opy_[item.nodeid].get(bstack1lllll1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⍜"), []))
                exception, bstack1lll11l1_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1lll11l1_opy_ = [call.excinfo.exconly(), getattr(report, bstack1lllll1l_opy_ (u"ࠩ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠨ⍝"), bstack1lllll1l_opy_ (u"ࠪࠫ⍞"))]
                bstack11lll1ll_opy_.stop(time=bstack11lllllll_opy_, result=Result(result=getattr(report, bstack1lllll1l_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬ⍟"), bstack1lllll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ⍠")), exception=exception, bstack1lll11l1_opy_=bstack1lll11l1_opy_))
                bstack1ll1l1l1_opy_.bstack1lll11ll_opy_(bstack1lllll1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ⍡"), _1ll1l111_opy_[item.nodeid][bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ⍢")])
        elif getattr(report, bstack1lllll1l_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭⍣"), bstack1lllll1l_opy_ (u"ࠩࠪ⍤")) in [bstack1lllll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ⍥"), bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭⍦")]:
            logger.debug(bstack1lllll1l_opy_ (u"ࠬ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡵࡷࡥࡹ࡫ࠠ࠮ࠢࡾࢁ࠱ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠢ࠰ࠤࢀࢃࠧ⍧").format(getattr(report, bstack1lllll1l_opy_ (u"࠭ࡷࡩࡧࡱࠫ⍨"), bstack1lllll1l_opy_ (u"ࠧࠨ⍩")).__str__(), bstack1lll1ll1l111_opy_))
            bstack1l11ll1l_opy_ = item.nodeid + bstack1lllll1l_opy_ (u"ࠨ࠯ࠪ⍪") + getattr(report, bstack1lllll1l_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ⍫"), bstack1lllll1l_opy_ (u"ࠪࠫ⍬"))
            if getattr(report, bstack1lllll1l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ⍭"), False):
                hook_type = bstack1lllll1l_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪ⍮") if getattr(report, bstack1lllll1l_opy_ (u"࠭ࡷࡩࡧࡱࠫ⍯"), bstack1lllll1l_opy_ (u"ࠧࠨ⍰")) == bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⍱") else bstack1lllll1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭⍲")
                _1ll1l111_opy_[bstack1l11ll1l_opy_] = {
                    bstack1lllll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⍳"): uuid4().__str__(),
                    bstack1lllll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⍴"): bstack11lllllll_opy_,
                    bstack1lllll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⍵"): hook_type
                }
            _1ll1l111_opy_[bstack1l11ll1l_opy_][bstack1lllll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⍶")] = bstack11lllllll_opy_
            bstack1lll1lll1111_opy_(_1ll1l111_opy_[bstack1l11ll1l_opy_][bstack1lllll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⍷")])
            bstack1lll1lll111l_opy_(item, _1ll1l111_opy_[bstack1l11ll1l_opy_], bstack1lllll1l_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⍸"), report, call)
            if getattr(report, bstack1lllll1l_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ⍹"), bstack1lllll1l_opy_ (u"ࠪࠫ⍺")) == bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ⍻"):
                if getattr(report, bstack1lllll1l_opy_ (u"ࠬࡵࡵࡵࡥࡲࡱࡪ࠭⍼"), bstack1lllll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭⍽")) == bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⍾"):
                    bstack1ll1lll1_opy_ = {
                        bstack1lllll1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⍿"): uuid4().__str__(),
                        bstack1lllll1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⎀"): bstack1l1111ll_opy_(),
                        bstack1lllll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⎁"): bstack1l1111ll_opy_()
                    }
                    _1ll1l111_opy_[item.nodeid] = {**_1ll1l111_opy_[item.nodeid], **bstack1ll1lll1_opy_}
                    bstack1lll1lll11l1_opy_(item, _1ll1l111_opy_[item.nodeid], bstack1lllll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⎂"))
                    bstack1lll1lll11l1_opy_(item, _1ll1l111_opy_[item.nodeid], bstack1lllll1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⎃"), report, call)
    except Exception as err:
        print(bstack1lllll1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡽࢀࠫ⎄"), str(err))
def bstack1lll1lll11ll_opy_(test, bstack1ll1lll1_opy_, result=None, call=None, bstack111l111lll_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11lll1ll_opy_ = {
        bstack1lllll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⎅"): bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⎆")],
        bstack1lllll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⎇"): bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࠨ⎈"),
        bstack1lllll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⎉"): test.name,
        bstack1lllll1l_opy_ (u"ࠬࡨ࡯ࡥࡻࠪ⎊"): {
            bstack1lllll1l_opy_ (u"࠭࡬ࡢࡰࡪࠫ⎋"): bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ⎌"),
            bstack1lllll1l_opy_ (u"ࠨࡥࡲࡨࡪ࠭⎍"): inspect.getsource(test.obj)
        },
        bstack1lllll1l_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭⎎"): test.name,
        bstack1lllll1l_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩ⎏"): test.name,
        bstack1lllll1l_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫ⎐"): bstack1ll11l1l_opy_.bstack1ll11111_opy_(test),
        bstack1lllll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ⎑"): file_path,
        bstack1lllll1l_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨ⎒"): file_path,
        bstack1lllll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⎓"): bstack1lllll1l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⎔"),
        bstack1lllll1l_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧ⎕"): file_path,
        bstack1lllll1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⎖"): bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⎗")],
        bstack1lllll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ⎘"): bstack1lllll1l_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭⎙"),
        bstack1lllll1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪ⎚"): {
            bstack1lllll1l_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬ⎛"): test.nodeid
        },
        bstack1lllll1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ⎜"): bstack111l1l1l1l1_opy_(test.own_markers)
    }
    if bstack111l111lll_opy_ in [bstack1lllll1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫ⎝"), bstack1lllll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭⎞")]:
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠬࡳࡥࡵࡣࠪ⎟")] = {
            bstack1lllll1l_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ⎠"): bstack1ll1lll1_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⎡"), [])
        }
    if bstack111l111lll_opy_ == bstack1lllll1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩ⎢"):
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⎣")] = bstack1lllll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ⎤")
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⎥")] = bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⎦")]
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⎧")] = bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎨")]
    if result:
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⎩")] = result.outcome
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ⎪")] = result.duration * 1000
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⎫")] = bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⎬")]
        if result.failed:
            bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ⎭")] = bstack1ll1l1l1_opy_.bstack111111l111_opy_(call.excinfo.typename)
            bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ⎮")] = bstack1ll1l1l1_opy_.bstack1llll1l11111_opy_(call.excinfo, result)
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⎯")] = bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⎰")]
    if outcome:
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⎱")] = bstack1111l11l1l1_opy_(outcome)
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ⎲")] = 0
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⎳")] = bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⎴")]
        if bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⎵")] == bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⎶"):
            bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⎷")] = bstack1lllll1l_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪ⎸")  # bstack1lll1lll1l11_opy_
            bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ⎹")] = [{bstack1lllll1l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ⎺"): [bstack1lllll1l_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩ⎻")]}]
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⎼")] = bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⎽")]
    return bstack11lll1ll_opy_
def bstack1lll1ll11l11_opy_(test, bstack1l11l1ll_opy_, bstack111l111lll_opy_, result, call, outcome, bstack1lll1ll11l1l_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ⎾")]
    hook_name = bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬ⎿")]
    hook_data = {
        bstack1lllll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⏀"): bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"ࠫࡺࡻࡩࡥࠩ⏁")],
        bstack1lllll1l_opy_ (u"ࠬࡺࡹࡱࡧࠪ⏂"): bstack1lllll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⏃"),
        bstack1lllll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⏄"): bstack1lllll1l_opy_ (u"ࠨࡽࢀࠫ⏅").format(bstack11l111l1ll1_opy_(hook_name)),
        bstack1lllll1l_opy_ (u"ࠩࡥࡳࡩࡿࠧ⏆"): {
            bstack1lllll1l_opy_ (u"ࠪࡰࡦࡴࡧࠨ⏇"): bstack1lllll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ⏈"),
            bstack1lllll1l_opy_ (u"ࠬࡩ࡯ࡥࡧࠪ⏉"): None
        },
        bstack1lllll1l_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬ⏊"): test.name,
        bstack1lllll1l_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧ⏋"): bstack1ll11l1l_opy_.bstack1ll11111_opy_(test, hook_name),
        bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ⏌"): file_path,
        bstack1lllll1l_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫ⏍"): file_path,
        bstack1lllll1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⏎"): bstack1lllll1l_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ⏏"),
        bstack1lllll1l_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪ⏐"): file_path,
        bstack1lllll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⏑"): bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⏒")],
        bstack1lllll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ⏓"): bstack1lllll1l_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫ⏔") if bstack1lll1ll1l111_opy_ == bstack1lllll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧ⏕") else bstack1lllll1l_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫ⏖"),
        bstack1lllll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⏗"): hook_type
    }
    bstack1l111ll1111_opy_ = bstack1ll1l1ll_opy_(_1ll1l111_opy_.get(test.nodeid, None))
    if bstack1l111ll1111_opy_:
        hook_data[bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫ⏘")] = bstack1l111ll1111_opy_
    if result:
        hook_data[bstack1lllll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⏙")] = result.outcome
        hook_data[bstack1lllll1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩ⏚")] = result.duration * 1000
        hook_data[bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⏛")] = bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⏜")]
        if result.failed:
            hook_data[bstack1lllll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪ⏝")] = bstack1ll1l1l1_opy_.bstack111111l111_opy_(call.excinfo.typename)
            hook_data[bstack1lllll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭⏞")] = bstack1ll1l1l1_opy_.bstack1llll1l11111_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack1lllll1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⏟")] = bstack1111l11l1l1_opy_(outcome)
        hook_data[bstack1lllll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ⏠")] = 100
        hook_data[bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⏡")] = bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⏢")]
        if hook_data[bstack1lllll1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⏣")] == bstack1lllll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⏤"):
            hook_data[bstack1lllll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ⏥")] = bstack1lllll1l_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧ⏦")  # bstack1lll1lll1l11_opy_
            hook_data[bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ⏧")] = [{bstack1lllll1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ⏨"): [bstack1lllll1l_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭⏩")]}]
    if bstack1lll1ll11l1l_opy_:
        hook_data[bstack1lllll1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⏪")] = bstack1lll1ll11l1l_opy_.result
        hook_data[bstack1lllll1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⏫")] = bstack111l11ll1l1_opy_(bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⏬")], bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⏭")])
        hook_data[bstack1lllll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⏮")] = bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⏯")]
        if hook_data[bstack1lllll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⏰")] == bstack1lllll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⏱"):
            hook_data[bstack1lllll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪ⏲")] = bstack1ll1l1l1_opy_.bstack111111l111_opy_(bstack1lll1ll11l1l_opy_.exception_type)
            hook_data[bstack1lllll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭⏳")] = [{bstack1lllll1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ⏴"): bstack1111lll11l1_opy_(bstack1lll1ll11l1l_opy_.exception)}]
    return hook_data
def bstack1lll1lll11l1_opy_(test, bstack1ll1lll1_opy_, bstack111l111lll_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack1lllll1l_opy_ (u"ࠧࡴࡧࡱࡨࡤࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡦࡸࡨࡲࡹࡀࠠࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡷࡩࡸࡺࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࠦ࠭ࠡࡽࢀࠫ⏵").format(bstack111l111lll_opy_))
    bstack11lll1ll_opy_ = bstack1lll1lll11ll_opy_(test, bstack1ll1lll1_opy_, result, call, bstack111l111lll_opy_, outcome)
    driver = getattr(test, bstack1lllll1l_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ⏶"), None)
    if bstack111l111lll_opy_ == bstack1lllll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⏷") and driver:
        bstack11lll1ll_opy_[bstack1lllll1l_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩ⏸")] = bstack1ll1l1l1_opy_.bstack1ll111l1_opy_(driver)
    if bstack111l111lll_opy_ == bstack1lllll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬ⏹"):
        bstack111l111lll_opy_ = bstack1lllll1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⏺")
    bstack1ll111ll_opy_ = {
        bstack1lllll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⏻"): bstack111l111lll_opy_,
        bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ⏼"): bstack11lll1ll_opy_
    }
    bstack1ll1l1l1_opy_.bstack1l111111_opy_(bstack1ll111ll_opy_)
    if bstack111l111lll_opy_ == bstack1lllll1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⏽"):
        threading.current_thread().bstackTestMeta = {bstack1lllll1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ⏾"): bstack1lllll1l_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ⏿")}
    elif bstack111l111lll_opy_ == bstack1lllll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭␀"):
        threading.current_thread().bstackTestMeta = {bstack1lllll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ␁"): getattr(result, bstack1lllll1l_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧ␂"), bstack1lllll1l_opy_ (u"ࠧࠨ␃"))}
def bstack1lll1lll111l_opy_(test, bstack1ll1lll1_opy_, bstack111l111lll_opy_, result=None, call=None, outcome=None, bstack1lll1ll11l1l_opy_=None):
    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡵࡨࡲࡩࡥࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡧࡹࡩࡳࡺ࠺ࠡࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣ࡬ࡴࡵ࡫ࠡࡦࡤࡸࡦ࠲ࠠࡦࡸࡨࡲࡹ࡚ࡹࡱࡧࠣ࠱ࠥࢁࡽࠨ␄").format(bstack111l111lll_opy_))
    hook_data = bstack1lll1ll11l11_opy_(test, bstack1ll1lll1_opy_, bstack111l111lll_opy_, result, call, outcome, bstack1lll1ll11l1l_opy_)
    bstack1ll111ll_opy_ = {
        bstack1lllll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭␅"): bstack111l111lll_opy_,
        bstack1lllll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࠬ␆"): hook_data
    }
    bstack1ll1l1l1_opy_.bstack1l111111_opy_(bstack1ll111ll_opy_)
def bstack1ll1l1ll_opy_(bstack1ll1lll1_opy_):
    if not bstack1ll1lll1_opy_:
        return None
    if bstack1ll1lll1_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ␇"), None):
        return getattr(bstack1ll1lll1_opy_[bstack1lllll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ␈")], bstack1lllll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ␉"), None)
    return bstack1ll1lll1_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ␊"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.LOG, bstack1lll1lll111_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_.LOG, bstack1lll1lll111_opy_.POST, request, caplog)
        return # skip all existing operations
    try:
        if not bstack1ll1l1l1_opy_.on():
            return
        places = [bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ␋"), bstack1lllll1l_opy_ (u"ࠩࡦࡥࡱࡲࠧ␌"), bstack1lllll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬ␍")]
        logs = []
        for bstack1lll1llll111_opy_ in places:
            records = caplog.get_records(bstack1lll1llll111_opy_)
            bstack1llll11111l1_opy_ = bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ␎") if bstack1lll1llll111_opy_ == bstack1lllll1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ␏") else bstack1lllll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭␐")
            bstack1lll1lll1l1l_opy_ = request.node.nodeid + (bstack1lllll1l_opy_ (u"ࠧࠨ␑") if bstack1lll1llll111_opy_ == bstack1lllll1l_opy_ (u"ࠨࡥࡤࡰࡱ࠭␒") else bstack1lllll1l_opy_ (u"ࠩ࠰ࠫ␓") + bstack1lll1llll111_opy_)
            test_uuid = bstack1ll1l1ll_opy_(_1ll1l111_opy_.get(bstack1lll1lll1l1l_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack111l111l1l1_opy_(record.message):
                    continue
                logs.append({
                    bstack1lllll1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭␔"): bstack1111l111lll_opy_(record.created).isoformat() + bstack1lllll1l_opy_ (u"ࠫ࡟࠭␕"),
                    bstack1lllll1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ␖"): record.levelname,
                    bstack1lllll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ␗"): record.message,
                    bstack1llll11111l1_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1ll1l1l1_opy_.bstack1ll1llll_opy_(logs)
    except Exception as err:
        print(bstack1lllll1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡥࡲࡲࡩࡥࡦࡪࡺࡷࡹࡷ࡫࠺ࠡࡽࢀࠫ␘"), str(err))
def bstack111l1ll1l_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1ll1ll1111_opy_
    bstack1ll1ll1l1_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ␙"), None) and bstack1l11l1l1_opy_(
            threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ␚"), None)
    bstack111lll1111_opy_ = getattr(driver, bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ␛"), None) != None and getattr(driver, bstack1lllll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ␜"), None) == True
    if sequence == bstack1lllll1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ␝") and driver != None:
      if not bstack1ll1ll1111_opy_ and bstack1lll1ll11ll_opy_() and bstack1lllll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭␞") in CONFIG and CONFIG[bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ␟")] == True and bstack11l11l11ll_opy_.bstack1l1lll1l1_opy_(driver_command) and (bstack111lll1111_opy_ or bstack1ll1ll1l1_opy_) and not bstack11l1111l1_opy_(args):
        try:
          bstack1ll1ll1111_opy_ = True
          logger.debug(bstack1lllll1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡼࡿࠪ␠").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack1lllll1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡥࡳࡨࡲࡶࡲࠦࡳࡤࡣࡱࠤࢀࢃࠧ␡").format(str(err)))
        bstack1ll1ll1111_opy_ = False
    if sequence == bstack1lllll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩ␢"):
        if driver_command == bstack1lllll1l_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ␣"):
            bstack1ll1l1l1_opy_.bstack11111llll1_opy_({
                bstack1lllll1l_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ␤"): response[bstack1lllll1l_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ␥")],
                bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ␦"): store[bstack1lllll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ␧")]
            })
def bstack11l11111l_opy_():
    global bstack1111lll11l_opy_
    bstack11llll111l_opy_.bstack11ll11l1ll_opy_()
    logging.shutdown()
    bstack1ll1l1l1_opy_.bstack1l11lll1_opy_()
    for driver in bstack1111lll11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1llllll1_opy_(*args):
    global bstack1111lll11l_opy_
    bstack1ll1l1l1_opy_.bstack1l11lll1_opy_()
    for driver in bstack1111lll11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1lll11lll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1ll1111l11_opy_(self, *args, **kwargs):
    bstack111l1l1111_opy_ = bstack1l11ll1ll1_opy_(self, *args, **kwargs)
    bstack11l1lll1l1_opy_ = getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪ␨"), None)
    if bstack11l1lll1l1_opy_ and bstack11l1lll1l1_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ␩"), bstack1lllll1l_opy_ (u"ࠫࠬ␪")) == bstack1lllll1l_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭␫"):
        bstack1ll1l1l1_opy_.bstack1111ll11ll_opy_(self)
    return bstack111l1l1111_opy_
@measure(event_name=EVENTS.bstack1l111llll_opy_, stage=STAGE.bstack1l1l11111l_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack11lllll1l_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
    if bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ␬")):
        return
    bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ␭"), True)
    global bstack1l11ll11l1_opy_
    global bstack1l11l11l1l_opy_
    bstack1l11ll11l1_opy_ = framework_name
    logger.info(bstack111l1lll1_opy_.format(bstack1l11ll11l1_opy_.split(bstack1lllll1l_opy_ (u"ࠨ࠯ࠪ␮"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1lll1ll11ll_opy_():
            Service.start = bstack1ll1l1lll_opy_
            Service.stop = bstack11l1111ll_opy_
            webdriver.Remote.get = bstack1l1111111_opy_
            webdriver.Remote.__init__ = bstack11l1l111ll_opy_
            if not isinstance(os.getenv(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪ␯")), str):
                return
            WebDriver.quit = bstack1ll1ll1ll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1ll1l1l1_opy_.on():
            webdriver.Remote.__init__ = bstack1ll1111l11_opy_
        bstack1l11l11l1l_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡗࡊࡒࡅࡏࡋࡘࡑࡤࡕࡒࡠࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡏࡎࡔࡖࡄࡐࡑࡋࡄࠨ␰")):
        bstack1l11l11l1l_opy_ = eval(os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩ␱")))
    if not bstack1l11l11l1l_opy_:
        bstack1l1ll11ll1_opy_(bstack1lllll1l_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢ␲"), bstack1llll1ll11_opy_)
    if bstack11lll111l1_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack1lllll1l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ␳")) and callable(getattr(RemoteConnection, bstack1lllll1l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ␴"))):
                RemoteConnection._get_proxy_url = bstack11111l1ll1_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack11111l1ll1_opy_
        except Exception as e:
            logger.error(bstack11lll11l1_opy_.format(str(e)))
    if bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ␵") in str(framework_name).lower():
        if not bstack1lll1ll11ll_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1l11111l1l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1ll1ll1l_opy_
            Config.getoption = bstack11l1ll111_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack11l1111ll1_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l111lll1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1ll1ll1ll_opy_(self):
    global bstack1l11ll11l1_opy_
    global bstack11llll1lll_opy_
    global bstack1lll1l1lll_opy_
    try:
        if bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ␶") in bstack1l11ll11l1_opy_ and self.session_id != None and bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧ␷"), bstack1lllll1l_opy_ (u"ࠫࠬ␸")) != bstack1lllll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭␹"):
            bstack111ll1l1l_opy_ = bstack1lllll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭␺") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ␻")
            bstack111ll1lll_opy_(logger, True)
            if os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫ␼"), None):
                self.execute_script(
                    bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ␽") + json.dumps(
                        os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭␾"))) + bstack1lllll1l_opy_ (u"ࠫࢂࢃࠧ␿"))
            if self != None:
                bstack1l1ll1l11_opy_(self, bstack111ll1l1l_opy_, bstack1lllll1l_opy_ (u"ࠬ࠲ࠠࠨ⑀").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1l11llll1l1_opy_(bstack1l1l111llll_opy_):
            item = store.get(bstack1lllll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⑁"), None)
            if item is not None and bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭⑂"), None):
                bstack111ll11l_opy_.bstack111l111l_opy_(self, bstack1lll111111_opy_, logger, item)
        threading.current_thread().testStatus = bstack1lllll1l_opy_ (u"ࠨࠩ⑃")
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࠥ⑄") + str(e))
    bstack1lll1l1lll_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1l1l111ll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack11l1l111ll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack11llll1lll_opy_
    global bstack1l1ll1l1l1_opy_
    global bstack11l11l1ll1_opy_
    global bstack1l11ll11l1_opy_
    global bstack1l11ll1ll1_opy_
    global bstack1111lll11l_opy_
    global bstack11lll1111_opy_
    global bstack1l1l1l111_opy_
    global bstack1lll111111_opy_
    CONFIG[bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ⑅")] = str(bstack1l11ll11l1_opy_) + str(__version__)
    command_executor = bstack11l1l11lll_opy_(bstack11lll1111_opy_, CONFIG)
    logger.debug(bstack11l1l1l1ll_opy_.format(command_executor))
    proxy = bstack1111111ll_opy_(CONFIG, proxy)
    bstack11ll1l1ll_opy_ = 0
    try:
        if bstack11l11l1ll1_opy_ is True:
            bstack11ll1l1ll_opy_ = int(os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ⑆")))
    except:
        bstack11ll1l1ll_opy_ = 0
    bstack11111lllll_opy_ = bstack11111lll1_opy_(CONFIG, bstack11ll1l1ll_opy_)
    logger.debug(bstack11l1lll11l_opy_.format(str(bstack11111lllll_opy_)))
    bstack1lll111111_opy_ = CONFIG.get(bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⑇"))[bstack11ll1l1ll_opy_]
    if bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ⑈") in CONFIG and CONFIG[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ⑉")]:
        bstack1llll1l1l1_opy_(bstack11111lllll_opy_, bstack1l1l1l111_opy_)
    if bstack1111ll1l_opy_.bstack1l1lll1l1l_opy_(CONFIG, bstack11ll1l1ll_opy_) and bstack1111ll1l_opy_.bstack1l1l1l1ll_opy_(bstack11111lllll_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1l11llll1l1_opy_(bstack1l1l111llll_opy_):
            bstack1111ll1l_opy_.set_capabilities(bstack11111lllll_opy_, CONFIG)
    if desired_capabilities:
        bstack1l11ll11ll_opy_ = bstack11lllll11_opy_(desired_capabilities)
        bstack1l11ll11ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ⑊")] = bstack111ll1l11_opy_(CONFIG)
        bstack11l1l1l1l1_opy_ = bstack11111lll1_opy_(bstack1l11ll11ll_opy_)
        if bstack11l1l1l1l1_opy_:
            bstack11111lllll_opy_ = update(bstack11l1l1l1l1_opy_, bstack11111lllll_opy_)
        desired_capabilities = None
    if options:
        bstack1lll11l1l1_opy_(options, bstack11111lllll_opy_)
    if not options:
        options = bstack1l1l11l111_opy_(bstack11111lllll_opy_)
    if proxy and bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ⑋")):
        options.proxy(proxy)
    if options and bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ⑌")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l111llll1_opy_() < version.parse(bstack1lllll1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ⑍")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack11111lllll_opy_)
    logger.info(bstack1111l11l1_opy_)
    bstack111l1111l_opy_.end(EVENTS.bstack1l111llll_opy_.value, EVENTS.bstack1l111llll_opy_.value + bstack1lllll1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ⑎"),
                               EVENTS.bstack1l111llll_opy_.value + bstack1lllll1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ⑏"), True, None)
    try:
        if bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧ⑐")):
            bstack1l11ll1ll1_opy_(self, command_executor=command_executor,
                      options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
        elif bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ⑑")):
            bstack1l11ll1ll1_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities, options=options,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        elif bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩ⑒")):
            bstack1l11ll1ll1_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        else:
            bstack1l11ll1ll1_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive)
    except Exception as bstack1l1111111l_opy_:
        logger.error(bstack11lll1ll1_opy_.format(bstack1lllll1l_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠩ⑓"), str(bstack1l1111111l_opy_)))
        raise bstack1l1111111l_opy_
    try:
        bstack1llll11l1l_opy_ = bstack1lllll1l_opy_ (u"ࠫࠬ⑔")
        if bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭⑕")):
            bstack1llll11l1l_opy_ = self.caps.get(bstack1lllll1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨ⑖"))
        else:
            bstack1llll11l1l_opy_ = self.capabilities.get(bstack1lllll1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ⑗"))
        if bstack1llll11l1l_opy_:
            bstack1l11ll111l_opy_(bstack1llll11l1l_opy_)
            if bstack1l111llll1_opy_() <= version.parse(bstack1lllll1l_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨ⑘")):
                self.command_executor._url = bstack1lllll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ⑙") + bstack11lll1111_opy_ + bstack1lllll1l_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢ⑚")
            else:
                self.command_executor._url = bstack1lllll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨ⑛") + bstack1llll11l1l_opy_ + bstack1lllll1l_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨ⑜")
            logger.debug(bstack111l111l1_opy_.format(bstack1llll11l1l_opy_))
        else:
            logger.debug(bstack1ll11ll11l_opy_.format(bstack1lllll1l_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢ⑝")))
    except Exception as e:
        logger.debug(bstack1ll11ll11l_opy_.format(e))
    bstack11llll1lll_opy_ = self.session_id
    if bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ⑞") in bstack1l11ll11l1_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack1lllll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ⑟"), None)
        if item:
            bstack1lll1ll1lll1_opy_ = getattr(item, bstack1lllll1l_opy_ (u"ࠩࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪࡥࡳࡵࡣࡵࡸࡪࡪࠧ①"), False)
            if not getattr(item, bstack1lllll1l_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫ②"), None) and bstack1lll1ll1lll1_opy_:
                setattr(store[bstack1lllll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ③")], bstack1lllll1l_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭④"), self)
        bstack11l1lll1l1_opy_ = getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧ⑤"), None)
        if bstack11l1lll1l1_opy_ and bstack11l1lll1l1_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⑥"), bstack1lllll1l_opy_ (u"ࠨࠩ⑦")) == bstack1lllll1l_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪ⑧"):
            bstack1ll1l1l1_opy_.bstack1111ll11ll_opy_(self)
    bstack1111lll11l_opy_.append(self)
    if bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭⑨") in CONFIG and bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⑩") in CONFIG[bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⑪")][bstack11ll1l1ll_opy_]:
        bstack1l1ll1l1l1_opy_ = CONFIG[bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⑫")][bstack11ll1l1ll_opy_][bstack1lllll1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⑬")]
    logger.debug(bstack111l1l1ll1_opy_.format(bstack11llll1lll_opy_))
@measure(event_name=EVENTS.bstack11lll1l1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1l1111111_opy_(self, url):
    global bstack1ll1ll1l11_opy_
    global CONFIG
    try:
        bstack1l11l1111_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack111lll1ll1_opy_.format(str(err)))
    try:
        bstack1ll1ll1l11_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack11ll11l1l1_opy_):
                bstack1l11l1111_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack111lll1ll1_opy_.format(str(err)))
        raise e
def bstack1l11l111l_opy_(item, when):
    global bstack1lllllllll_opy_
    try:
        bstack1lllllllll_opy_(item, when)
    except Exception as e:
        pass
def bstack11l1111ll1_opy_(item, call, rep):
    global bstack11111l11l1_opy_
    global bstack1111lll11l_opy_
    name = bstack1lllll1l_opy_ (u"ࠨࠩ⑭")
    try:
        if rep.when == bstack1lllll1l_opy_ (u"ࠩࡦࡥࡱࡲࠧ⑮"):
            bstack11llll1lll_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack1lllll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⑯"))
            try:
                if (str(skipSessionName).lower() != bstack1lllll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩ⑰")):
                    name = str(rep.nodeid)
                    bstack111l1l1lll_opy_ = bstack111lll1l11_opy_(bstack1lllll1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⑱"), name, bstack1lllll1l_opy_ (u"࠭ࠧ⑲"), bstack1lllll1l_opy_ (u"ࠧࠨ⑳"), bstack1lllll1l_opy_ (u"ࠨࠩ⑴"), bstack1lllll1l_opy_ (u"ࠩࠪ⑵"))
                    os.environ[bstack1lllll1l_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭⑶")] = name
                    for driver in bstack1111lll11l_opy_:
                        if bstack11llll1lll_opy_ == driver.session_id:
                            driver.execute_script(bstack111l1l1lll_opy_)
            except Exception as e:
                logger.debug(bstack1lllll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ⑷").format(str(e)))
            try:
                bstack11ll11llll_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack1lllll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭⑸"):
                    status = bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭⑹") if rep.outcome.lower() == bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⑺") else bstack1lllll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⑻")
                    reason = bstack1lllll1l_opy_ (u"ࠩࠪ⑼")
                    if status == bstack1lllll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⑽"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack1lllll1l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ⑾") if status == bstack1lllll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ⑿") else bstack1lllll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⒀")
                    data = name + bstack1lllll1l_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩ⒁") if status == bstack1lllll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⒂") else name + bstack1lllll1l_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬ⒃") + reason
                    bstack111l11lll_opy_ = bstack111lll1l11_opy_(bstack1lllll1l_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ⒄"), bstack1lllll1l_opy_ (u"ࠫࠬ⒅"), bstack1lllll1l_opy_ (u"ࠬ࠭⒆"), bstack1lllll1l_opy_ (u"࠭ࠧ⒇"), level, data)
                    for driver in bstack1111lll11l_opy_:
                        if bstack11llll1lll_opy_ == driver.session_id:
                            driver.execute_script(bstack111l11lll_opy_)
            except Exception as e:
                logger.debug(bstack1lllll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ⒈").format(str(e)))
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬ⒉").format(str(e)))
    bstack11111l11l1_opy_(item, call, rep)
notset = Notset()
def bstack11l1ll111_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11111l1lll_opy_
    if str(name).lower() == bstack1lllll1l_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩ⒊"):
        return bstack1lllll1l_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤ⒋")
    else:
        return bstack11111l1lll_opy_(self, name, default, skip)
def bstack11111l1ll1_opy_(self):
    global CONFIG
    global bstack1lll1ll111_opy_
    try:
        proxy = bstack111l11ll1_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack1lllll1l_opy_ (u"ࠫ࠳ࡶࡡࡤࠩ⒌")):
                proxies = bstack11l1111lll_opy_(proxy, bstack11l1l11lll_opy_())
                if len(proxies) > 0:
                    protocol, bstack11ll1l1lll_opy_ = proxies.popitem()
                    if bstack1lllll1l_opy_ (u"ࠧࡀ࠯࠰ࠤ⒍") in bstack11ll1l1lll_opy_:
                        return bstack11ll1l1lll_opy_
                    else:
                        return bstack1lllll1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ⒎") + bstack11ll1l1lll_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack1lllll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡴࡷࡵࡸࡺࠢࡸࡶࡱࠦ࠺ࠡࡽࢀࠦ⒏").format(str(e)))
    return bstack1lll1ll111_opy_(self)
def bstack11lll111l1_opy_():
    return (bstack1lllll1l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ⒐") in CONFIG or bstack1lllll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭⒑") in CONFIG) and bstack111ll1111l_opy_() and bstack1l111llll1_opy_() >= version.parse(
        bstack1l1l1l1lll_opy_)
def bstack1l11llll1l_opy_(self,
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
    global bstack1l1ll1l1l1_opy_
    global bstack11l11l1ll1_opy_
    global bstack1l11ll11l1_opy_
    CONFIG[bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ⒒")] = str(bstack1l11ll11l1_opy_) + str(__version__)
    bstack11ll1l1ll_opy_ = 0
    try:
        if bstack11l11l1ll1_opy_ is True:
            bstack11ll1l1ll_opy_ = int(os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ⒓")))
    except:
        bstack11ll1l1ll_opy_ = 0
    CONFIG[bstack1lllll1l_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ⒔")] = True
    bstack11111lllll_opy_ = bstack11111lll1_opy_(CONFIG, bstack11ll1l1ll_opy_)
    logger.debug(bstack11l1lll11l_opy_.format(str(bstack11111lllll_opy_)))
    if CONFIG.get(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ⒕")):
        bstack1llll1l1l1_opy_(bstack11111lllll_opy_, bstack1l1l1l111_opy_)
    if bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⒖") in CONFIG and bstack1lllll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⒗") in CONFIG[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⒘")][bstack11ll1l1ll_opy_]:
        bstack1l1ll1l1l1_opy_ = CONFIG[bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭⒙")][bstack11ll1l1ll_opy_][bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⒚")]
    import urllib
    import json
    if bstack1lllll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⒛") in CONFIG and str(CONFIG[bstack1lllll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ⒜")]).lower() != bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭⒝"):
        bstack11ll11l11l_opy_ = bstack1l1ll1lll1_opy_()
        bstack1l111ll111_opy_ = bstack11ll11l11l_opy_ + urllib.parse.quote(json.dumps(bstack11111lllll_opy_))
    else:
        bstack1l111ll111_opy_ = bstack1lllll1l_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪ⒞") + urllib.parse.quote(json.dumps(bstack11111lllll_opy_))
    browser = self.connect(bstack1l111ll111_opy_)
    return browser
def bstack1l1111ll11_opy_():
    global bstack1l11l11l1l_opy_
    global bstack1l11ll11l1_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack111l111ll_opy_
        if not bstack1lll1ll11ll_opy_():
            global bstack111llllll1_opy_
            if not bstack111llllll1_opy_:
                from bstack_utils.helper import bstack1ll11l1ll_opy_, bstack11ll1ll111_opy_
                bstack111llllll1_opy_ = bstack1ll11l1ll_opy_()
                bstack11ll1ll111_opy_(bstack1l11ll11l1_opy_)
            BrowserType.connect = bstack111l111ll_opy_
            return
        BrowserType.launch = bstack1l11llll1l_opy_
        bstack1l11l11l1l_opy_ = True
    except Exception as e:
        pass
def bstack1lll1llll1l1_opy_():
    global CONFIG
    global bstack1l1111l11l_opy_
    global bstack11lll1111_opy_
    global bstack1l1l1l111_opy_
    global bstack11l11l1ll1_opy_
    global bstack111l1ll11_opy_
    CONFIG = json.loads(os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨ⒟")))
    bstack1l1111l11l_opy_ = eval(os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ⒠")))
    bstack11lll1111_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫ⒡"))
    bstack111111l1l1_opy_(CONFIG, bstack1l1111l11l_opy_)
    bstack111l1ll11_opy_ = bstack11llll111l_opy_.configure_logger(CONFIG, bstack111l1ll11_opy_)
    if cli.bstack11111l1l1_opy_():
        bstack1l11l1lll_opy_.invoke(Events.CONNECT, bstack111lllllll_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ⒢"), bstack1lllll1l_opy_ (u"࠭࠰ࠨ⒣")))
        cli.bstack1l1l111l1l1_opy_(cli_context.platform_index)
        cli.bstack1l1l1l1ll1l_opy_(bstack11l1l11lll_opy_(bstack11lll1111_opy_, CONFIG), cli_context.platform_index, bstack1l1l11l111_opy_)
        cli.bstack1l1l1111l1l_opy_()
        logger.debug(bstack1lllll1l_opy_ (u"ࠢࡄࡎࡌࠤ࡮ࡹࠠࡢࡥࡷ࡭ࡻ࡫ࠠࡧࡱࡵࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࠨ⒤") + str(cli_context.platform_index) + bstack1lllll1l_opy_ (u"ࠣࠤ⒥"))
        return # skip all existing operations
    global bstack1l11ll1ll1_opy_
    global bstack1lll1l1lll_opy_
    global bstack11l1l1llll_opy_
    global bstack1ll11l11l_opy_
    global bstack1llll1l1ll_opy_
    global bstack1l1ll1lll_opy_
    global bstack1111l11lll_opy_
    global bstack1ll1ll1l11_opy_
    global bstack1lll1ll111_opy_
    global bstack11111l1lll_opy_
    global bstack1lllllllll_opy_
    global bstack11111l11l1_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1l11ll1ll1_opy_ = webdriver.Remote.__init__
        bstack1lll1l1lll_opy_ = WebDriver.quit
        bstack1111l11lll_opy_ = WebDriver.close
        bstack1ll1ll1l11_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack1lllll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ⒦") in CONFIG or bstack1lllll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ⒧") in CONFIG) and bstack111ll1111l_opy_():
        if bstack1l111llll1_opy_() < version.parse(bstack1l1l1l1lll_opy_):
            logger.error(bstack1lllllll11_opy_.format(bstack1l111llll1_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack1lllll1l_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ⒨")) and callable(getattr(RemoteConnection, bstack1lllll1l_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭⒩"))):
                    bstack1lll1ll111_opy_ = RemoteConnection._get_proxy_url
                else:
                    from selenium.webdriver.remote.client_config import ClientConfig
                    bstack1lll1ll111_opy_ = ClientConfig.get_proxy_url
            except Exception as e:
                logger.error(bstack11lll11l1_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack11111l1lll_opy_ = Config.getoption
        from _pytest import runner
        bstack1lllllllll_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1111l111_opy_)
    try:
        from pytest_bdd import reporting
        bstack11111l11l1_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧ⒪"))
    bstack1l1l1l111_opy_ = CONFIG.get(bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ⒫"), {}).get(bstack1lllll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ⒬"))
    bstack11l11l1ll1_opy_ = True
    bstack11lllll1l_opy_(bstack1l11111lll_opy_)
if (bstack111l1111ll1_opy_()):
    bstack1lll1llll1l1_opy_()
@error_handler(class_method=False)
def bstack1lll1ll1l11l_opy_(hook_name, event, bstack1ll11l1l11l_opy_=None):
    if hook_name not in [bstack1lllll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪ⒭"), bstack1lllll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧ⒮"), bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪ⒯"), bstack1lllll1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧ⒰"), bstack1lllll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫ⒱"), bstack1lllll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨ⒲"), bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧ⒳"), bstack1lllll1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫ⒴")]:
        return
    node = store[bstack1lllll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ⒵")]
    if hook_name in [bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪⒶ"), bstack1lllll1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧⒷ")]:
        node = store[bstack1lllll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡪࡶࡨࡱࠬⒸ")]
    elif hook_name in [bstack1lllll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬⒹ"), bstack1lllll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩⒺ")]:
        node = store[bstack1lllll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡧࡱࡧࡳࡴࡡ࡬ࡸࡪࡳࠧⒻ")]
    hook_type = bstack11l111l1l11_opy_(hook_name)
    if event == bstack1lllll1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪⒼ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_[hook_type], bstack1lll1lll111_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack1l11l1ll_opy_ = {
            bstack1lllll1l_opy_ (u"ࠫࡺࡻࡩࡥࠩⒽ"): uuid,
            bstack1lllll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩⒾ"): bstack1l1111ll_opy_(),
            bstack1lllll1l_opy_ (u"࠭ࡴࡺࡲࡨࠫⒿ"): bstack1lllll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࠬⓀ"),
            bstack1lllll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫⓁ"): hook_type,
            bstack1lllll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬⓂ"): hook_name
        }
        store[bstack1lllll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧⓃ")].append(uuid)
        bstack1lll1lll1lll_opy_ = node.nodeid
        if hook_type == bstack1lllll1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩⓄ"):
            if not _1ll1l111_opy_.get(bstack1lll1lll1lll_opy_, None):
                _1ll1l111_opy_[bstack1lll1lll1lll_opy_] = {bstack1lllll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫⓅ"): []}
            _1ll1l111_opy_[bstack1lll1lll1lll_opy_][bstack1lllll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬⓆ")].append(bstack1l11l1ll_opy_[bstack1lllll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬⓇ")])
        _1ll1l111_opy_[bstack1lll1lll1lll_opy_ + bstack1lllll1l_opy_ (u"ࠨ࠯ࠪⓈ") + hook_name] = bstack1l11l1ll_opy_
        bstack1lll1lll111l_opy_(node, bstack1l11l1ll_opy_, bstack1lllll1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪⓉ"))
    elif event == bstack1lllll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩⓊ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll111l1l_opy_[hook_type], bstack1lll1lll111_opy_.POST, node, None, bstack1ll11l1l11l_opy_)
            return
        bstack1l11ll1l_opy_ = node.nodeid + bstack1lllll1l_opy_ (u"ࠫ࠲࠭Ⓥ") + hook_name
        _1ll1l111_opy_[bstack1l11ll1l_opy_][bstack1lllll1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪⓌ")] = bstack1l1111ll_opy_()
        bstack1lll1lll1111_opy_(_1ll1l111_opy_[bstack1l11ll1l_opy_][bstack1lllll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫⓍ")])
        bstack1lll1lll111l_opy_(node, _1ll1l111_opy_[bstack1l11ll1l_opy_], bstack1lllll1l_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩⓎ"), bstack1lll1ll11l1l_opy_=bstack1ll11l1l11l_opy_)
def bstack1lll1llll11l_opy_():
    global bstack1lll1ll1l111_opy_
    if bstack11l1ll11l1_opy_():
        bstack1lll1ll1l111_opy_ = bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬⓏ")
    else:
        bstack1lll1ll1l111_opy_ = bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩⓐ")
def pytest_collection_modifyitems(session, config, items):
    bstack1lllll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡊ࡮ࡲࡴࡦࡴࡶࠤࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡱࡻࡷࡩࡸࡺࠠࡪࡶࡨࡱࡸࠦࡢࡢࡵࡨࡨࠥࡵ࡮ࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸࡪࡪࠠࡴࡧ࡯ࡩࡨࡺ࡯ࡳࡵࠣࡪࡷࡵ࡭ࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡶࡻ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤⓑ")
    import os
    bstack1lll1llll1ll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡓࡗࡉࡈࡆࡕࡗࡖࡆ࡚ࡅࡅࡡࡖࡉࡑࡋࡃࡕࡑࡕࡗࠬⓒ"))
    logger.info(bstack1lllll1l_opy_ (u"ࠧࡡࡰࡺࡶࡨࡷࡹࡥࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࡢࡱࡴࡪࡩࡧࡻ࡬ࡸࡪࡳࡳ࡞ࠢࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡫ࡤࠡࡵࡨࡰࡪࡩࡴࡰࡴࡶࠤ࡯ࡹ࡯࡯ࠢࡵࡩࡨ࡫ࡩࡷࡧࡧ࠾ࠥࢁࡽࠣⓓ").format(bstack1lll1llll1ll_opy_))
    if not bstack1lll1llll1ll_opy_:
        return
    try:
        bstack1lll1ll111l1_opy_ = json.loads(bstack1lll1llll1ll_opy_)
        if not isinstance(bstack1lll1ll111l1_opy_, (list, set)) or not bstack1lll1ll111l1_opy_:
            return
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠨࡃࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡳࡥࡷࡹࡥࠡࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡐࡔࡆࡌࡊ࡙ࡔࡓࡃࡗࡉࡉࡥࡓࡆࡎࡈࡇ࡙ࡕࡒࡔ࠼ࠣࠦⓔ") + str(e) + bstack1lllll1l_opy_ (u"ࠢࠣⓕ"))
        return
    selected = []
    deselected = []
    logger.info(bstack1lllll1l_opy_ (u"ࠣ࡝ࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࡥ࡭ࡰࡦ࡬ࡪࡾ࡯ࡴࡦ࡯ࡶࡡࠥࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤࡸ࡫࡬ࡦࡥࡷࡳࡷࡹࠠࡳࡧࡦࡩ࡮ࡼࡥࡥ࠼ࠣࡿࢂࠨⓖ").format(bstack1lll1ll111l1_opy_))
    bstack1lll1ll1l1ll_opy_ = set()
    for selector in bstack1lll1ll111l1_opy_:
        if not selector or not isinstance(selector, str):
            continue
        bstack1lll1ll1l1ll_opy_.add(selector)
    for item in items:
        nodeid = getattr(item, bstack1lllll1l_opy_ (u"ࠩࡱࡳࡩ࡫ࡩࡥࠩⓗ"), None)
        if not nodeid:
            deselected.append(item)
            continue
        if (
            nodeid in bstack1lll1ll1l1ll_opy_ or
            any(sel in nodeid for sel in bstack1lll1ll1l1ll_opy_)
        ):
            selected.append(item)
        else:
            deselected.append(item)
    if deselected:
        logger.info(bstack1lllll1l_opy_ (u"ࠥ࡟ࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࡠ࡯ࡲࡨ࡮࡬ࡹࡪࡶࡨࡱࡸࡣࠠࡅࡧࡶࡩࡱ࡫ࡣࡵࡧࡧࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢⓘ").format(deselected))
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected
@bstack1ll1l1l1_opy_.bstack1llll11l1ll1_opy_
def bstack1lll1lll1ll1_opy_():
    bstack1lll1llll11l_opy_()
    if cli.is_running():
        try:
            bstack11l1l1lllll_opy_(bstack1lll1ll1l11l_opy_)
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡴࠢࡳࡥࡹࡩࡨ࠻ࠢࡾࢁࠧⓙ").format(e))
        return
    if bstack111ll1111l_opy_():
        bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
        bstack1lllll1l_opy_ (u"ࠬ࠭ࠧࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡆࡰࡴࠣࡴࡵࡶࠠ࠾ࠢ࠴࠰ࠥࡳ࡯ࡥࡡࡨࡼࡪࡩࡵࡵࡧࠣ࡫ࡪࡺࡳࠡࡷࡶࡩࡩࠦࡦࡰࡴࠣࡥ࠶࠷ࡹࠡࡥࡲࡱࡲࡧ࡮ࡥࡵ࠰ࡻࡷࡧࡰࡱ࡫ࡱ࡫ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡊࡴࡸࠠࡱࡲࡳࠤࡃࠦ࠱࠭ࠢࡰࡳࡩࡥࡥࡹࡧࡦࡹࡹ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡵࡹࡳࠦࡢࡦࡥࡤࡹࡸ࡫ࠠࡪࡶࠣ࡭ࡸࠦࡰࡢࡶࡦ࡬ࡪࡪࠠࡪࡰࠣࡥࠥࡪࡩࡧࡨࡨࡶࡪࡴࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࠢ࡬ࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭ࡻࡳࠡࡹࡨࠤࡳ࡫ࡥࡥࠢࡷࡳࠥࡻࡳࡦࠢࡖࡩࡱ࡫࡮ࡪࡷࡰࡔࡦࡺࡣࡩࠪࡶࡩࡱ࡫࡮ࡪࡷࡰࡣ࡭ࡧ࡮ࡥ࡮ࡨࡶ࠮ࠦࡦࡰࡴࠣࡴࡵࡶࠠ࠿ࠢ࠴ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭ࠧࠨⓚ")
        if bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪⓛ")):
            if CONFIG.get(bstack1lllll1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧⓜ")) is not None and int(CONFIG[bstack1lllll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨⓝ")]) > 1:
                bstack11ll1ll11_opy_(bstack111l1ll1l_opy_)
            return
        bstack11ll1ll11_opy_(bstack111l1ll1l_opy_)
    try:
        bstack11l1l1lllll_opy_(bstack1lll1ll1l11l_opy_)
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࡹࠠࡱࡣࡷࡧ࡭ࡀࠠࡼࡿࠥⓞ").format(e))
bstack1lll1lll1ll1_opy_()