# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack11l1l1111l_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1lll11l1l1_opy_, bstack11l1l1llll_opy_, update, bstack11ll11l111_opy_,
                                       bstack1lll1ll111_opy_, bstack11l1l1ll11_opy_, bstack11l11ll1ll_opy_, bstack1l11lll11_opy_,
                                       bstack111l1l11l_opy_, bstack1ll1ll1ll1_opy_, bstack111lll1ll_opy_,
                                       bstack11l111ll11_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack11111111l_opy_)
from browserstack_sdk.bstack1111ll1l_opy_ import bstack11l11ll1_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack111l11l1l_opy_
from bstack_utils.capture import bstack1l111l11_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack11ll111ll1_opy_, bstack11ll1l1ll_opy_, bstack1l1ll11ll1_opy_, \
    bstack1111lllll1_opy_
from bstack_utils.helper import bstack1l1l1l1l_opy_, bstack1111l1l1l11_opy_, bstack1l11111l_opy_, bstack111l1l11ll_opy_, bstack1llll1111ll_opy_, bstack1ll1llll_opy_, \
    bstack1111ll111ll_opy_, \
    bstack1111lllll1l_opy_, bstack1ll1ll11ll_opy_, bstack111ll1ll1l_opy_, bstack1111ll11111_opy_, bstack1l1l1lll1_opy_, Notset, \
    bstack1111lll1l1_opy_, bstack111l11l1lll_opy_, bstack1111l1lll11_opy_, Result, bstack111l1llll1l_opy_, bstack1111ll1l1l1_opy_, error_handler, \
    bstack11ll1l11ll_opy_, bstack1l111llll1_opy_, bstack111ll11ll_opy_, bstack1111llllll1_opy_
from bstack_utils.bstack11l1ll11l11_opy_ import bstack11l1ll11l1l_opy_
from bstack_utils.messages import bstack1lll111ll1_opy_, bstack1111l1lll1_opy_, bstack1lllll1lll_opy_, bstack11l1l111ll_opy_, bstack11l11l11_opy_, \
    bstack11111l11l1_opy_, bstack1ll1l1l11_opy_, bstack1llll1lll1_opy_, bstack11llllllll_opy_, bstack11111ll1l_opy_, \
    bstack1l1111lll1_opy_, bstack1ll11l11l1_opy_, bstack111l1l1lll_opy_
from bstack_utils.proxy import bstack11lll11ll_opy_, bstack11l111llll_opy_
from bstack_utils.bstack111l111ll_opy_ import bstack11l11l11111_opy_, bstack11l111ll11l_opy_, bstack11l11l111l1_opy_, bstack11l11l1111l_opy_, \
    bstack11l111lll1l_opy_, bstack11l111lll11_opy_, bstack11l111ll1ll_opy_, bstack1ll1ll1ll_opy_, bstack11l111lllll_opy_
from bstack_utils.bstack1llll1l1ll_opy_ import bstack1lll1l111l_opy_
from bstack_utils.bstack1l111l11ll_opy_ import bstack1l11llll1_opy_, bstack11l1lll1l1_opy_, bstack11llll1111_opy_, \
    bstack111lll1111_opy_, bstack1111l1ll11_opy_
from bstack_utils.bstack1l1l111l_opy_ import bstack1l1111ll_opy_
from bstack_utils.bstack11llllll_opy_ import bstack1l11lll1_opy_
import bstack_utils.accessibility as bstack1lll1ll1l_opy_
from bstack_utils.bstack1ll1l11l_opy_ import bstack1l11ll1l_opy_
from bstack_utils.bstack1l11111ll_opy_ import bstack1l11111ll_opy_
from bstack_utils.bstack11l111l1_opy_ import bstack1111llll_opy_
from browserstack_sdk.__init__ import bstack111l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1l1l111l1l1_opy_ import bstack1l1l1l1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll111ll_opy_ import bstack1llll111ll_opy_, Events, bstack1lll1l1l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1l1llllll1l_opy_, bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1llll111ll_opy_ import bstack1llll111ll_opy_, Events, bstack1lll1l1l1l_opy_
bstack1l111ll111_opy_ = None
bstack11ll11lll1_opy_ = None
bstack1l1l11l1ll_opy_ = None
bstack11ll111111_opy_ = None
bstack11l1ll1111_opy_ = None
bstack1l1ll1111_opy_ = None
bstack11lllll1l1_opy_ = None
bstack1l111111ll_opy_ = None
bstack11llll11l_opy_ = None
bstack1111l1ll1l_opy_ = None
bstack111l1llll1_opy_ = None
bstack1l11111l11_opy_ = None
bstack111l1ll1l_opy_ = None
bstack1l1ll111l1_opy_ = bstack1l1lll1_opy_ (u"ࠨࠩ≒")
CONFIG = {}
bstack1l1lllllll_opy_ = False
bstack1l111lllll_opy_ = bstack1l1lll1_opy_ (u"ࠩࠪ≓")
bstack1111l11l1_opy_ = bstack1l1lll1_opy_ (u"ࠪࠫ≔")
bstack11lll1111l_opy_ = False
bstack1l11l1111l_opy_ = []
bstack1111ll1ll_opy_ = bstack11ll111ll1_opy_
bstack1llll1111l1l_opy_ = bstack1l1lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ≕")
bstack1ll1l1l1l_opy_ = {}
bstack1lll111l11_opy_ = None
bstack111lllll1_opy_ = False
logger = bstack111l11l1l_opy_.get_logger(__name__, bstack1111ll1ll_opy_)
store = {
    bstack1l1lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ≖"): []
}
bstack1lll1lllllll_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1l11l1l1_opy_ = {}
current_test_uuid = None
cli_context = bstack1l1llllll1l_opy_(
    test_framework_name=bstack1111l1111_opy_[bstack1l1lll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪ≗")] if bstack1l1l1lll1_opy_() else bstack1111l1111_opy_[bstack1l1lll1_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚ࠧ≘")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack1l1ll1l111_opy_(page, bstack1l1111l1l_opy_):
    try:
        page.evaluate(bstack1l1lll1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ≙"),
                      bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭≚") + json.dumps(
                          bstack1l1111l1l_opy_) + bstack1l1lll1_opy_ (u"ࠥࢁࢂࠨ≛"))
    except Exception as e:
        print(bstack1l1lll1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤ≜"), e)
def bstack11l1l11l1l_opy_(page, message, level):
    try:
        page.evaluate(bstack1l1lll1_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ≝"), bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ≞") + json.dumps(
            message) + bstack1l1lll1_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪ≟") + json.dumps(level) + bstack1l1lll1_opy_ (u"ࠨࡿࢀࠫ≠"))
    except Exception as e:
        print(bstack1l1lll1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧ≡"), e)
def pytest_configure(config):
    global bstack1l111lllll_opy_
    global CONFIG
    bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
    config.args = bstack1l11lll1_opy_.bstack11l11l11ll1_opy_(config.args)
    bstack1111111l_opy_.bstack1l11111111_opy_(bstack111ll11ll_opy_(config.getoption(bstack1l1lll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ≢"))))
    try:
        bstack111l11l1l_opy_.bstack11111lll11l_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack1llll111ll_opy_.invoke(Events.CONNECT, bstack1lll1l1l1l_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ≣"), bstack1l1lll1_opy_ (u"ࠬ࠶ࠧ≤")))
        config = json.loads(os.environ.get(bstack1l1lll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠧ≥"), bstack1l1lll1_opy_ (u"ࠢࡼࡿࠥ≦")))
        cli.bstack1l1l11l1l1l_opy_(bstack111ll1ll1l_opy_(bstack1l111lllll_opy_, CONFIG), cli_context.platform_index, bstack11ll11l111_opy_)
    if cli.bstack1l1l111111l_opy_(bstack1l1l1l1ll1l_opy_):
        cli.bstack1l1l1ll111l_opy_()
        logger.debug(bstack1l1lll1_opy_ (u"ࠣࡅࡏࡍࠥ࡯ࡳࠡࡣࡦࡸ࡮ࡼࡥࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢ≧") + str(cli_context.platform_index) + bstack1l1lll1_opy_ (u"ࠤࠥ≨"))
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.BEFORE_ALL, bstack1lll1lll11l_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack1l1lll1_opy_ (u"ࠥࡻ࡭࡫࡮ࠣ≩"), None)
    if cli.is_running() and when == bstack1l1lll1_opy_ (u"ࠦࡨࡧ࡬࡭ࠤ≪"):
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.LOG_REPORT, bstack1lll1lll11l_opy_.PRE, item, call)
    outcome = yield
    if when == bstack1l1lll1_opy_ (u"ࠧࡩࡡ࡭࡮ࠥ≫"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1lll1_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣ≬")))
        if not passed:
            config = json.loads(os.environ.get(bstack1l1lll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࠨ≭"), bstack1l1lll1_opy_ (u"ࠣࡽࢀࠦ≮")))
            if bstack1111llll_opy_.bstack1lll1l1ll_opy_(config):
                bstack1lllll1lll11_opy_ = bstack1111llll_opy_.bstack1lllll111_opy_(config)
                if item.execution_count > bstack1lllll1lll11_opy_:
                    print(bstack1l1lll1_opy_ (u"ࠩࡗࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡲࡦࡶࡵ࡭ࡪࡹ࠺ࠡࠩ≯"), report.nodeid, os.environ.get(bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ≰")))
                    bstack1111llll_opy_.bstack111lll11lll_opy_(report.nodeid)
            else:
                print(bstack1l1lll1_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࠫ≱"), report.nodeid, os.environ.get(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ≲")))
                bstack1111llll_opy_.bstack111lll11lll_opy_(report.nodeid)
        else:
            print(bstack1l1lll1_opy_ (u"࠭ࡔࡦࡵࡷࠤࡵࡧࡳࡴࡧࡧ࠾ࠥ࠭≳"), report.nodeid, os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ≴")))
    if cli.is_running():
        if when == bstack1l1lll1_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢ≵"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.BEFORE_EACH, bstack1lll1lll11l_opy_.POST, item, call, outcome)
        elif when == bstack1l1lll1_opy_ (u"ࠤࡦࡥࡱࡲࠢ≶"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.LOG_REPORT, bstack1lll1lll11l_opy_.POST, item, call, outcome)
        elif when == bstack1l1lll1_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧ≷"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.AFTER_EACH, bstack1lll1lll11l_opy_.POST, item, call, outcome)
        return # skip all existing operations
    skipSessionName = item.config.getoption(bstack1l1lll1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭≸"))
    plugins = item.config.getoption(bstack1l1lll1_opy_ (u"ࠧࡶ࡬ࡶࡩ࡬ࡲࡸࠨ≹"))
    report = outcome.get_result()
    os.environ[bstack1l1lll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ≺")] = report.nodeid
    bstack1lll1ll1ll1l_opy_(item, call, report)
    if bstack1l1lll1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡶ࡬ࡶࡩ࡬ࡲࠧ≻") not in plugins or bstack1l1l1lll1_opy_():
        return
    summary = []
    driver = getattr(item, bstack1l1lll1_opy_ (u"ࠣࡡࡧࡶ࡮ࡼࡥࡳࠤ≼"), None)
    page = getattr(item, bstack1l1lll1_opy_ (u"ࠤࡢࡴࡦ࡭ࡥࠣ≽"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1lll1llll11l_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1lll1llll111_opy_(item, report, summary, skipSessionName)
def bstack1lll1llll11l_opy_(item, report, summary, skipSessionName):
    if report.when == bstack1l1lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ≾") and report.skipped:
        bstack11l111lllll_opy_(report)
    if report.when in [bstack1l1lll1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥ≿"), bstack1l1lll1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢ⊀")]:
        return
    if not bstack1llll1111ll_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack1l1lll1_opy_ (u"࠭ࡴࡳࡷࡨࠫ⊁")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬ⊂") + json.dumps(
                    report.nodeid) + bstack1l1lll1_opy_ (u"ࠨࡿࢀࠫ⊃"))
        os.environ[bstack1l1lll1_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬ⊄")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack1l1lll1_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩ࠿ࠦࡻ࠱ࡿࠥ⊅").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1lll1_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨ⊆")))
    bstack111ll1l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨ⊇")
    bstack11l111lllll_opy_(report)
    if not passed:
        try:
            bstack111ll1l1ll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack1l1lll1_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨ⊈").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack111ll1l1ll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack1l1lll1_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤ⊉")))
        bstack111ll1l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠣࠤ⊊")
        if not passed:
            try:
                bstack111ll1l1ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l1lll1_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤ⊋").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack111ll1l1ll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡤࡢࡶࡤࠦ࠿ࠦࠧ⊌")
                    + json.dumps(bstack1l1lll1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠥࠧ⊍"))
                    + bstack1l1lll1_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣ⊎")
                )
            else:
                item._driver.execute_script(
                    bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫ⊏")
                    + json.dumps(str(bstack111ll1l1ll_opy_))
                    + bstack1l1lll1_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥ⊐")
                )
        except Exception as e:
            summary.append(bstack1l1lll1_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡡ࡯ࡰࡲࡸࡦࡺࡥ࠻ࠢࡾ࠴ࢂࠨ⊑").format(e))
def bstack1lll1ll1l1ll_opy_(test_name, error_message):
    try:
        bstack1llll111l111_opy_ = []
        bstack1l11l1lll_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ⊒"), bstack1l1lll1_opy_ (u"ࠪ࠴ࠬ⊓"))
        bstack11lll1111_opy_ = {bstack1l1lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⊔"): test_name, bstack1l1lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ⊕"): error_message, bstack1l1lll1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ⊖"): bstack1l11l1lll_opy_}
        bstack1llll11111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ⊗"))
        if os.path.exists(bstack1llll11111ll_opy_):
            with open(bstack1llll11111ll_opy_) as f:
                bstack1llll111l111_opy_ = json.load(f)
        bstack1llll111l111_opy_.append(bstack11lll1111_opy_)
        with open(bstack1llll11111ll_opy_, bstack1l1lll1_opy_ (u"ࠨࡹࠪ⊘")) as f:
            json.dump(bstack1llll111l111_opy_, f)
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵ࡫ࡲࡴ࡫ࡶࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡶࡹࡵࡧࡶࡸࠥ࡫ࡲࡳࡱࡵࡷ࠿ࠦࠧ⊙") + str(e))
def bstack1lll1llll111_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack1l1lll1_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤ⊚"), bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ⊛")]:
        return
    if (str(skipSessionName).lower() != bstack1l1lll1_opy_ (u"ࠬࡺࡲࡶࡧࠪ⊜")):
        bstack1l1ll1l111_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1lll1_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣ⊝")))
    bstack111ll1l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠢࠣ⊞")
    bstack11l111lllll_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack111ll1l1ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l1lll1_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣ⊟").format(e)
                )
        try:
            if passed:
                bstack1111l1ll11_opy_(getattr(item, bstack1l1lll1_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨ⊠"), None), bstack1l1lll1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ⊡"))
            else:
                error_message = bstack1l1lll1_opy_ (u"ࠫࠬ⊢")
                if bstack111ll1l1ll_opy_:
                    bstack11l1l11l1l_opy_(item._page, str(bstack111ll1l1ll_opy_), bstack1l1lll1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ⊣"))
                    bstack1111l1ll11_opy_(getattr(item, bstack1l1lll1_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬ⊤"), None), bstack1l1lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ⊥"), str(bstack111ll1l1ll_opy_))
                    error_message = str(bstack111ll1l1ll_opy_)
                else:
                    bstack1111l1ll11_opy_(getattr(item, bstack1l1lll1_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧ⊦"), None), bstack1l1lll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ⊧"))
                bstack1lll1ll1l1ll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack1l1lll1_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿ࠵ࢃࠢ⊨").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack1l1lll1_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ⊩"), default=bstack1l1lll1_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦ⊪"), help=bstack1l1lll1_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧ⊫"))
    parser.addoption(bstack1l1lll1_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨ⊬"), default=bstack1l1lll1_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢ⊭"), help=bstack1l1lll1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣ⊮"))
    parser.addoption(bstack1l1lll1_opy_ (u"ࠪ࠱࠲ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡭࡮ࡨࡧࡹ࠳࡮ࡰࡦࡨ࡭ࡩࡹࠧ⊯"), action=bstack1l1lll1_opy_ (u"ࠫࡸࡺ࡯ࡳࡧࡢࡸࡷࡻࡥࠨ⊰"), default=False, help=bstack1l1lll1_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮࠾ࠥࡉ࡯࡭࡮ࡨࡧࡹࠦࡡ࡯ࡦࠣࡴࡷ࡯࡮ࡵࠢࡷࡩࡸࡺࠠ࡯ࡱࡧࡩ࡮ࡪࡳࠡ࡫ࡱࠤࡨࡲࡥࡢࡰࠣࡪࡴࡸ࡭ࡢࡶ࠯ࠤࡹ࡮ࡥ࡯ࠢࡨࡼ࡮ࡺࠧ⊱"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack1l1lll1_opy_ (u"ࠨ࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠣ⊲"), action=bstack1l1lll1_opy_ (u"ࠢࡴࡶࡲࡶࡪࠨ⊳"), default=bstack1l1lll1_opy_ (u"ࠣࡥ࡫ࡶࡴࡳࡥࠣ⊴"),
                         help=bstack1l1lll1_opy_ (u"ࠤࡇࡶ࡮ࡼࡥࡳࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳࠣ⊵"))
def bstack11lllll1_opy_(log):
    if not (log[bstack1l1lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⊶")] and log[bstack1l1lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⊷")].strip()):
        return
    active = bstack1ll1lll1_opy_()
    log = {
        bstack1l1lll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⊸"): log[bstack1l1lll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⊹")],
        bstack1l1lll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⊺"): bstack1l11111l_opy_().isoformat() + bstack1l1lll1_opy_ (u"ࠨ࡜ࠪ⊻"),
        bstack1l1lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⊼"): log[bstack1l1lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⊽")],
    }
    if active:
        if active[bstack1l1lll1_opy_ (u"ࠫࡹࡿࡰࡦࠩ⊾")] == bstack1l1lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⊿"):
            log[bstack1l1lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⋀")] = active[bstack1l1lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⋁")]
        elif active[bstack1l1lll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭⋂")] == bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࠧ⋃"):
            log[bstack1l1lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⋄")] = active[bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⋅")]
    bstack1l11ll1l_opy_.bstack1l1l1111_opy_([log])
def bstack1ll1lll1_opy_():
    if len(store[bstack1l1lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⋆")]) > 0 and store[bstack1l1lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⋇")][-1]:
        return {
            bstack1l1lll1_opy_ (u"ࠧࡵࡻࡳࡩࠬ⋈"): bstack1l1lll1_opy_ (u"ࠨࡪࡲࡳࡰ࠭⋉"),
            bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⋊"): store[bstack1l1lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ⋋")][-1]
        }
    if store.get(bstack1l1lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ⋌"), None):
        return {
            bstack1l1lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪ⋍"): bstack1l1lll1_opy_ (u"࠭ࡴࡦࡵࡷࠫ⋎"),
            bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⋏"): store[bstack1l1lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⋐")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.INIT_TEST, bstack1lll1lll11l_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.INIT_TEST, bstack1lll1lll11l_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1lll1lll1ll1_opy_ = True
        bstack11lll11l1_opy_ = bstack1lll1ll1l_opy_.bstack1ll11111l1_opy_(bstack1111lllll1l_opy_(item.own_markers))
        if not cli.bstack1l1l111111l_opy_(bstack1l1l1l1ll1l_opy_):
            item._a11y_test_case = bstack11lll11l1_opy_
            if bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ⋑"), None):
                driver = getattr(item, bstack1l1lll1_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫ⋒"), None)
                item._a11y_started = bstack1lll1ll1l_opy_.bstack11lllll111_opy_(driver, bstack11lll11l1_opy_)
        if not bstack1l11ll1l_opy_.on() or bstack1llll1111l1l_opy_ != bstack1l1lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ⋓"):
            return
        global current_test_uuid #, bstack1ll11111_opy_
        bstack1l11l1ll_opy_ = {
            bstack1l1lll1_opy_ (u"ࠬࡻࡵࡪࡦࠪ⋔"): uuid4().__str__(),
            bstack1l1lll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⋕"): bstack1l11111l_opy_().isoformat() + bstack1l1lll1_opy_ (u"࡛ࠧࠩ⋖")
        }
        current_test_uuid = bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⋗")]
        store[bstack1l1lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⋘")] = bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⋙")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l11l1l1_opy_[item.nodeid] = {**_1l11l1l1_opy_[item.nodeid], **bstack1l11l1ll_opy_}
        bstack1llll111l11l_opy_(item, _1l11l1l1_opy_[item.nodeid], bstack1l1lll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⋚"))
    except Exception as err:
        print(bstack1l1lll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡩࡡ࡭࡮࠽ࠤࢀࢃࠧ⋛"), str(err))
def pytest_runtest_setup(item):
    store[bstack1l1lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⋜")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.BEFORE_EACH, bstack1lll1lll11l_opy_.PRE, item, bstack1l1lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⋝"))
    if bstack1111llll_opy_.bstack111lll1l11l_opy_():
            bstack1lll1lll1lll_opy_ = bstack1l1lll1_opy_ (u"ࠣࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡣࡶࠤࡹ࡮ࡥࠡࡣࡥࡳࡷࡺࠠࡣࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡪࡾࡩࡴࡶࡶ࠲ࠧ⋞")
            logger.error(bstack1lll1lll1lll_opy_)
            bstack1l11l1ll_opy_ = {
                bstack1l1lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⋟"): uuid4().__str__(),
                bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⋠"): bstack1l11111l_opy_().isoformat() + bstack1l1lll1_opy_ (u"ࠫ࡟࠭⋡"),
                bstack1l1lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⋢"): bstack1l11111l_opy_().isoformat() + bstack1l1lll1_opy_ (u"࡚࠭ࠨ⋣"),
                bstack1l1lll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⋤"): bstack1l1lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ⋥"),
                bstack1l1lll1_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ⋦"): bstack1lll1lll1lll_opy_,
                bstack1l1lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⋧"): [],
                bstack1l1lll1_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭⋨"): []
            }
            bstack1llll111l11l_opy_(item, bstack1l11l1ll_opy_, bstack1l1lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭⋩"))
            pytest.skip(bstack1lll1lll1lll_opy_)
            return # skip all existing operations
    global bstack1lll1lllllll_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack1111ll11111_opy_():
        atexit.register(bstack1l11ll11l1_opy_)
        if not bstack1lll1lllllll_opy_:
            try:
                bstack1llll1111l11_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack1111llllll1_opy_():
                    bstack1llll1111l11_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1llll1111l11_opy_:
                    signal.signal(s, bstack1lll1ll1l1l1_opy_)
                bstack1lll1lllllll_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack1l1lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨ࡫࡮ࡹࡴࡦࡴࠣࡷ࡮࡭࡮ࡢ࡮ࠣ࡬ࡦࡴࡤ࡭ࡧࡵࡷ࠿ࠦࠢ⋪") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l11l11111_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack1l1lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⋫")
    try:
        if not bstack1l11ll1l_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack1l11l1ll_opy_ = {
            bstack1l1lll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⋬"): uuid,
            bstack1l1lll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⋭"): bstack1l11111l_opy_().isoformat() + bstack1l1lll1_opy_ (u"ࠪ࡞ࠬ⋮"),
            bstack1l1lll1_opy_ (u"ࠫࡹࡿࡰࡦࠩ⋯"): bstack1l1lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⋰"),
            bstack1l1lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩ⋱"): bstack1l1lll1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬ⋲"),
            bstack1l1lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫ⋳"): bstack1l1lll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ⋴")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack1l1lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ⋵")] = item
        store[bstack1l1lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⋶")] = [uuid]
        if not _1l11l1l1_opy_.get(item.nodeid, None):
            _1l11l1l1_opy_[item.nodeid] = {bstack1l1lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⋷"): [], bstack1l1lll1_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ⋸"): []}
        _1l11l1l1_opy_[item.nodeid][bstack1l1lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⋹")].append(bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⋺")])
        _1l11l1l1_opy_[item.nodeid + bstack1l1lll1_opy_ (u"ࠩ࠰ࡷࡪࡺࡵࡱࠩ⋻")] = bstack1l11l1ll_opy_
        bstack1lll1lllll1l_opy_(item, bstack1l11l1ll_opy_, bstack1l1lll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ⋼"))
    except Exception as err:
        print(bstack1l1lll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡸ࡫ࡴࡶࡲ࠽ࠤࢀࢃࠧ⋽"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.AFTER_EACH, bstack1lll1lll11l_opy_.PRE, item, bstack1l1lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ⋾"))
        return # skip all existing operations
    try:
        global bstack1ll1l1l1l_opy_
        bstack1l11l1lll_opy_ = 0
        if bstack11lll1111l_opy_ is True:
            bstack1l11l1lll_opy_ = int(os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭⋿")))
        if bstack11ll111l1l_opy_.bstack111ll11l11_opy_() == bstack1l1lll1_opy_ (u"ࠢࡵࡴࡸࡩࠧ⌀"):
            if bstack11ll111l1l_opy_.bstack11l1ll11l1_opy_() == bstack1l1lll1_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥ⌁"):
                bstack1lll1ll11l1l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⌂"), None)
                bstack11ll1l1ll1_opy_ = bstack1lll1ll11l1l_opy_ + bstack1l1lll1_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨ⌃")
                driver = getattr(item, bstack1l1lll1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ⌄"), None)
                bstack1111l11ll_opy_ = getattr(item, bstack1l1lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ⌅"), None)
                bstack1l1lll111l_opy_ = getattr(item, bstack1l1lll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⌆"), None)
                PercySDK.screenshot(driver, bstack11ll1l1ll1_opy_, bstack1111l11ll_opy_=bstack1111l11ll_opy_, bstack1l1lll111l_opy_=bstack1l1lll111l_opy_, bstack1l111l111l_opy_=bstack1l11l1lll_opy_)
        if not cli.bstack1l1l111111l_opy_(bstack1l1l1l1ll1l_opy_):
            if getattr(item, bstack1l1lll1_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡳࡵࡣࡵࡸࡪࡪࠧ⌇"), False):
                bstack11l11ll1_opy_.bstack1llllllll_opy_(getattr(item, bstack1l1lll1_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ⌈"), None), bstack1ll1l1l1l_opy_, logger, item)
        if not bstack1l11ll1l_opy_.on():
            return
        bstack1l11l1ll_opy_ = {
            bstack1l1lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⌉"): uuid4().__str__(),
            bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⌊"): bstack1l11111l_opy_().isoformat() + bstack1l1lll1_opy_ (u"ࠫ࡟࠭⌋"),
            bstack1l1lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪ⌌"): bstack1l1lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⌍"),
            bstack1l1lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ⌎"): bstack1l1lll1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬ⌏"),
            bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬ⌐"): bstack1l1lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬ⌑")
        }
        _1l11l1l1_opy_[item.nodeid + bstack1l1lll1_opy_ (u"ࠫ࠲ࡺࡥࡢࡴࡧࡳࡼࡴࠧ⌒")] = bstack1l11l1ll_opy_
        bstack1lll1lllll1l_opy_(item, bstack1l11l1ll_opy_, bstack1l1lll1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⌓"))
    except Exception as err:
        print(bstack1l1lll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮࠻ࠢࡾࢁࠬ⌔"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l11l1111l_opy_(fixturedef.argname):
        store[bstack1l1lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭⌕")] = request.node
    elif bstack11l111lll1l_opy_(fixturedef.argname):
        store[bstack1l1lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡦࡰࡦࡹࡳࡠ࡫ࡷࡩࡲ࠭⌖")] = request.node
    if not bstack1l11ll1l_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.SETUP_FIXTURE, bstack1lll1lll11l_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.SETUP_FIXTURE, bstack1lll1lll11l_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.SETUP_FIXTURE, bstack1lll1lll11l_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.SETUP_FIXTURE, bstack1lll1lll11l_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    try:
        fixture = {
            bstack1l1lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ⌗"): fixturedef.argname,
            bstack1l1lll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⌘"): bstack1111ll111ll_opy_(outcome),
            bstack1l1lll1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭⌙"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack1l1lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ⌚")]
        if not _1l11l1l1_opy_.get(current_test_item.nodeid, None):
            _1l11l1l1_opy_[current_test_item.nodeid] = {bstack1l1lll1_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ⌛"): []}
        _1l11l1l1_opy_[current_test_item.nodeid][bstack1l1lll1_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⌜")].append(fixture)
    except Exception as err:
        logger.debug(bstack1l1lll1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫ⌝"), str(err))
if bstack1l1l1lll1_opy_() and bstack1l11ll1l_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.STEP, bstack1lll1lll11l_opy_.PRE, request, step)
            return
        try:
            _1l11l1l1_opy_[request.node.nodeid][bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ⌞")].bstack11ll111l_opy_(id(step))
        except Exception as err:
            print(bstack1l1lll1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳ࠾ࠥࢁࡽࠨ⌟"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.STEP, bstack1lll1lll11l_opy_.POST, request, step, exception)
            return
        try:
            _1l11l1l1_opy_[request.node.nodeid][bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⌠")].bstack1l1l1ll1_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack1l1lll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩ⌡"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.STEP, bstack1lll1lll11l_opy_.POST, request, step)
            return
        try:
            bstack1l1l111l_opy_: bstack1l1111ll_opy_ = _1l11l1l1_opy_[request.node.nodeid][bstack1l1lll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ⌢")]
            bstack1l1l111l_opy_.bstack1l1l1ll1_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack1l1lll1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡷࡹ࡫ࡰࡠࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫ⌣"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1llll1111l1l_opy_
        try:
            if not bstack1l11ll1l_opy_.on() or bstack1llll1111l1l_opy_ != bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬ⌤"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ⌥"), None)
            if not _1l11l1l1_opy_.get(request.node.nodeid, None):
                _1l11l1l1_opy_[request.node.nodeid] = {}
            bstack1l1l111l_opy_ = bstack1l1111ll_opy_.bstack11111l11l1l_opy_(
                scenario, feature, request.node,
                name=bstack11l111lll11_opy_(request.node, scenario),
                started_at=bstack1ll1llll_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack1l1lll1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬ⌦"),
                tags=bstack11l111ll1ll_opy_(feature, scenario),
                bstack1ll11l11_opy_=bstack1l11ll1l_opy_.bstack1l111ll1_opy_(driver) if driver and driver.session_id else {}
            )
            _1l11l1l1_opy_[request.node.nodeid][bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⌧")] = bstack1l1l111l_opy_
            bstack1lll1llll1l1_opy_(bstack1l1l111l_opy_.uuid)
            bstack1l11ll1l_opy_.bstack1l1lllll_opy_(bstack1l1lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⌨"), bstack1l1l111l_opy_)
        except Exception as err:
            print(bstack1l1lll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨ〈"), str(err))
def bstack1lll1lll11ll_opy_(bstack11l1llll_opy_):
    if bstack11l1llll_opy_ in store[bstack1l1lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ〉")]:
        store[bstack1l1lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⌫")].remove(bstack11l1llll_opy_)
def bstack1lll1llll1l1_opy_(test_uuid):
    store[bstack1l1lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⌬")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1l11ll1l_opy_.bstack1llll1l1lll1_opy_
def bstack1lll1ll1ll1l_opy_(item, call, report):
    logger.debug(bstack1l1lll1_opy_ (u"ࠪ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡳࡵࡣࡵࡸࠬ⌭"))
    global bstack1llll1111l1l_opy_
    bstack1ll1l11l11_opy_ = bstack1ll1llll_opy_()
    if hasattr(report, bstack1l1lll1_opy_ (u"ࠫࡸࡺ࡯ࡱࠩ⌮")):
        bstack1ll1l11l11_opy_ = bstack111l1llll1l_opy_(report.stop)
    elif hasattr(report, bstack1l1lll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࠫ⌯")):
        bstack1ll1l11l11_opy_ = bstack111l1llll1l_opy_(report.start)
    try:
        if getattr(report, bstack1l1lll1_opy_ (u"࠭ࡷࡩࡧࡱࠫ⌰"), bstack1l1lll1_opy_ (u"ࠧࠨ⌱")) == bstack1l1lll1_opy_ (u"ࠨࡥࡤࡰࡱ࠭⌲"):
            logger.debug(bstack1l1lll1_opy_ (u"ࠩ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡹࡴࡢࡶࡨࠤ࠲ࠦࡻࡾ࠮ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦ࠭ࠡࡽࢀࠫ⌳").format(getattr(report, bstack1l1lll1_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⌴"), bstack1l1lll1_opy_ (u"ࠫࠬ⌵")).__str__(), bstack1llll1111l1l_opy_))
            if bstack1llll1111l1l_opy_ == bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ⌶"):
                _1l11l1l1_opy_[item.nodeid][bstack1l1lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⌷")] = bstack1ll1l11l11_opy_
                bstack1llll111l11l_opy_(item, _1l11l1l1_opy_[item.nodeid], bstack1l1lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⌸"), report, call)
                store[bstack1l1lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⌹")] = None
            elif bstack1llll1111l1l_opy_ == bstack1l1lll1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨ⌺"):
                bstack1l1l111l_opy_ = _1l11l1l1_opy_[item.nodeid][bstack1l1lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⌻")]
                bstack1l1l111l_opy_.set(hooks=_1l11l1l1_opy_[item.nodeid].get(bstack1l1lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⌼"), []))
                exception, bstack1l111l1l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l111l1l_opy_ = [call.excinfo.exconly(), getattr(report, bstack1l1lll1_opy_ (u"ࠬࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠫ⌽"), bstack1l1lll1_opy_ (u"࠭ࠧ⌾"))]
                bstack1l1l111l_opy_.stop(time=bstack1ll1l11l11_opy_, result=Result(result=getattr(report, bstack1l1lll1_opy_ (u"ࠧࡰࡷࡷࡧࡴࡳࡥࠨ⌿"), bstack1l1lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⍀")), exception=exception, bstack1l111l1l_opy_=bstack1l111l1l_opy_))
                bstack1l11ll1l_opy_.bstack1l1lllll_opy_(bstack1l1lll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⍁"), _1l11l1l1_opy_[item.nodeid][bstack1l1lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⍂")])
        elif getattr(report, bstack1l1lll1_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⍃"), bstack1l1lll1_opy_ (u"ࠬ࠭⍄")) in [bstack1l1lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ⍅"), bstack1l1lll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ⍆")]:
            logger.debug(bstack1l1lll1_opy_ (u"ࠨࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡸࡺࡡࡵࡧࠣ࠱ࠥࢁࡽ࠭ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࠳ࠠࡼࡿࠪ⍇").format(getattr(report, bstack1l1lll1_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ⍈"), bstack1l1lll1_opy_ (u"ࠪࠫ⍉")).__str__(), bstack1llll1111l1l_opy_))
            bstack1ll11l1l_opy_ = item.nodeid + bstack1l1lll1_opy_ (u"ࠫ࠲࠭⍊") + getattr(report, bstack1l1lll1_opy_ (u"ࠬࡽࡨࡦࡰࠪ⍋"), bstack1l1lll1_opy_ (u"࠭ࠧ⍌"))
            if getattr(report, bstack1l1lll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⍍"), False):
                hook_type = bstack1l1lll1_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭⍎") if getattr(report, bstack1l1lll1_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ⍏"), bstack1l1lll1_opy_ (u"ࠪࠫ⍐")) == bstack1l1lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ⍑") else bstack1l1lll1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩ⍒")
                _1l11l1l1_opy_[bstack1ll11l1l_opy_] = {
                    bstack1l1lll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⍓"): uuid4().__str__(),
                    bstack1l1lll1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⍔"): bstack1ll1l11l11_opy_,
                    bstack1l1lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ⍕"): hook_type
                }
            _1l11l1l1_opy_[bstack1ll11l1l_opy_][bstack1l1lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⍖")] = bstack1ll1l11l11_opy_
            bstack1lll1lll11ll_opy_(_1l11l1l1_opy_[bstack1ll11l1l_opy_][bstack1l1lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⍗")])
            bstack1lll1lllll1l_opy_(item, _1l11l1l1_opy_[bstack1ll11l1l_opy_], bstack1l1lll1_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭⍘"), report, call)
            if getattr(report, bstack1l1lll1_opy_ (u"ࠬࡽࡨࡦࡰࠪ⍙"), bstack1l1lll1_opy_ (u"࠭ࠧ⍚")) == bstack1l1lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⍛"):
                if getattr(report, bstack1l1lll1_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩ⍜"), bstack1l1lll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⍝")) == bstack1l1lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⍞"):
                    bstack1l11l1ll_opy_ = {
                        bstack1l1lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩ⍟"): uuid4().__str__(),
                        bstack1l1lll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⍠"): bstack1ll1llll_opy_(),
                        bstack1l1lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⍡"): bstack1ll1llll_opy_()
                    }
                    _1l11l1l1_opy_[item.nodeid] = {**_1l11l1l1_opy_[item.nodeid], **bstack1l11l1ll_opy_}
                    bstack1llll111l11l_opy_(item, _1l11l1l1_opy_[item.nodeid], bstack1l1lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ⍢"))
                    bstack1llll111l11l_opy_(item, _1l11l1l1_opy_[item.nodeid], bstack1l1lll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⍣"), report, call)
    except Exception as err:
        print(bstack1l1lll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࢀࢃࠧ⍤"), str(err))
def bstack1lll1lll111l_opy_(test, bstack1l11l1ll_opy_, result=None, call=None, bstack11l111ll1_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l1l111l_opy_ = {
        bstack1l1lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⍥"): bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩ⍦")],
        bstack1l1lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪ⍧"): bstack1l1lll1_opy_ (u"࠭ࡴࡦࡵࡷࠫ⍨"),
        bstack1l1lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⍩"): test.name,
        bstack1l1lll1_opy_ (u"ࠨࡤࡲࡨࡾ࠭⍪"): {
            bstack1l1lll1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧ⍫"): bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ⍬"),
            bstack1l1lll1_opy_ (u"ࠫࡨࡵࡤࡦࠩ⍭"): inspect.getsource(test.obj)
        },
        bstack1l1lll1_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ⍮"): test.name,
        bstack1l1lll1_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬ⍯"): test.name,
        bstack1l1lll1_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧ⍰"): bstack1l11lll1_opy_.bstack1l1ll11l_opy_(test),
        bstack1l1lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ⍱"): file_path,
        bstack1l1lll1_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫ⍲"): file_path,
        bstack1l1lll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⍳"): bstack1l1lll1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ⍴"),
        bstack1l1lll1_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪ⍵"): file_path,
        bstack1l1lll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⍶"): bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⍷")],
        bstack1l1lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ⍸"): bstack1l1lll1_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩ⍹"),
        bstack1l1lll1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭⍺"): {
            bstack1l1lll1_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨ⍻"): test.nodeid
        },
        bstack1l1lll1_opy_ (u"ࠬࡺࡡࡨࡵࠪ⍼"): bstack1111lllll1l_opy_(test.own_markers)
    }
    if bstack11l111ll1_opy_ in [bstack1l1lll1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧ⍽"), bstack1l1lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⍾")]:
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠨ࡯ࡨࡸࡦ࠭⍿")] = {
            bstack1l1lll1_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫ⎀"): bstack1l11l1ll_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ⎁"), [])
        }
    if bstack11l111ll1_opy_ == bstack1l1lll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬ⎂"):
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⎃")] = bstack1l1lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ⎄")
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⎅")] = bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⎆")]
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⎇")] = bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⎈")]
    if result:
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⎉")] = result.outcome
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭⎊")] = result.duration * 1000
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⎋")] = bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎌")]
        if result.failed:
            bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⎍")] = bstack1l11ll1l_opy_.bstack11111l1111_opy_(call.excinfo.typename)
            bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ⎎")] = bstack1l11ll1l_opy_.bstack1llll11ll1l1_opy_(call.excinfo, result)
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⎏")] = bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⎐")]
    if outcome:
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⎑")] = bstack1111ll111ll_opy_(outcome)
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ⎒")] = 0
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎓")] = bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⎔")]
        if bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⎕")] == bstack1l1lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⎖"):
            bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪ⎗")] = bstack1l1lll1_opy_ (u"࡛ࠬ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷ࠭⎘")  # bstack1lll1ll111l1_opy_
            bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ⎙")] = [{bstack1l1lll1_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪ⎚"): [bstack1l1lll1_opy_ (u"ࠨࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠬ⎛")]}]
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⎜")] = bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⎝")]
    return bstack1l1l111l_opy_
def bstack1lll1llll1ll_opy_(test, bstack1llll11l_opy_, bstack11l111ll1_opy_, result, call, outcome, bstack1lll1lll1l1l_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ⎞")]
    hook_name = bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨ⎟")]
    hook_data = {
        bstack1l1lll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⎠"): bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⎡")],
        bstack1l1lll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭⎢"): bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⎣"),
        bstack1l1lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨ⎤"): bstack1l1lll1_opy_ (u"ࠫࢀࢃࠧ⎥").format(bstack11l111ll11l_opy_(hook_name)),
        bstack1l1lll1_opy_ (u"ࠬࡨ࡯ࡥࡻࠪ⎦"): {
            bstack1l1lll1_opy_ (u"࠭࡬ࡢࡰࡪࠫ⎧"): bstack1l1lll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ⎨"),
            bstack1l1lll1_opy_ (u"ࠨࡥࡲࡨࡪ࠭⎩"): None
        },
        bstack1l1lll1_opy_ (u"ࠩࡶࡧࡴࡶࡥࠨ⎪"): test.name,
        bstack1l1lll1_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪ⎫"): bstack1l11lll1_opy_.bstack1l1ll11l_opy_(test, hook_name),
        bstack1l1lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ⎬"): file_path,
        bstack1l1lll1_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧ⎭"): file_path,
        bstack1l1lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⎮"): bstack1l1lll1_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ⎯"),
        bstack1l1lll1_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭⎰"): file_path,
        bstack1l1lll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⎱"): bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⎲")],
        bstack1l1lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ⎳"): bstack1l1lll1_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧ⎴") if bstack1llll1111l1l_opy_ == bstack1l1lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪ⎵") else bstack1l1lll1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧ⎶"),
        bstack1l1lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ⎷"): hook_type
    }
    bstack1l1111lll1l_opy_ = bstack1l1l1l11_opy_(_1l11l1l1_opy_.get(test.nodeid, None))
    if bstack1l1111lll1l_opy_:
        hook_data[bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡮ࡪࠧ⎸")] = bstack1l1111lll1l_opy_
    if result:
        hook_data[bstack1l1lll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⎹")] = result.outcome
        hook_data[bstack1l1lll1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⎺")] = result.duration * 1000
        hook_data[bstack1l1lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⎻")] = bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⎼")]
        if result.failed:
            hook_data[bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭⎽")] = bstack1l11ll1l_opy_.bstack11111l1111_opy_(call.excinfo.typename)
            hook_data[bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ⎾")] = bstack1l11ll1l_opy_.bstack1llll11ll1l1_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack1l1lll1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⎿")] = bstack1111ll111ll_opy_(outcome)
        hook_data[bstack1l1lll1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ⏀")] = 100
        hook_data[bstack1l1lll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏁")] = bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏂")]
        if hook_data[bstack1l1lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⏃")] == bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⏄"):
            hook_data[bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⏅")] = bstack1l1lll1_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪ⏆")  # bstack1lll1ll111l1_opy_
            hook_data[bstack1l1lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ⏇")] = [{bstack1l1lll1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ⏈"): [bstack1l1lll1_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩ⏉")]}]
    if bstack1lll1lll1l1l_opy_:
        hook_data[bstack1l1lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⏊")] = bstack1lll1lll1l1l_opy_.result
        hook_data[bstack1l1lll1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ⏋")] = bstack111l11l1lll_opy_(bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⏌")], bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⏍")])
        hook_data[bstack1l1lll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⏎")] = bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏏")]
        if hook_data[bstack1l1lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⏐")] == bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭⏑"):
            hook_data[bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭⏒")] = bstack1l11ll1l_opy_.bstack11111l1111_opy_(bstack1lll1lll1l1l_opy_.exception_type)
            hook_data[bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ⏓")] = [{bstack1l1lll1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ⏔"): bstack1111l1lll11_opy_(bstack1lll1lll1l1l_opy_.exception)}]
    return hook_data
def bstack1llll111l11l_opy_(test, bstack1l11l1ll_opy_, bstack11l111ll1_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack1l1lll1_opy_ (u"ࠪࡷࡪࡴࡤࡠࡶࡨࡷࡹࡥࡲࡶࡰࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡺࡥࡴࡶࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠢ࠰ࠤࢀࢃࠧ⏕").format(bstack11l111ll1_opy_))
    bstack1l1l111l_opy_ = bstack1lll1lll111l_opy_(test, bstack1l11l1ll_opy_, result, call, bstack11l111ll1_opy_, outcome)
    driver = getattr(test, bstack1l1lll1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ⏖"), None)
    if bstack11l111ll1_opy_ == bstack1l1lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⏗") and driver:
        bstack1l1l111l_opy_[bstack1l1lll1_opy_ (u"࠭ࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠬ⏘")] = bstack1l11ll1l_opy_.bstack1l111ll1_opy_(driver)
    if bstack11l111ll1_opy_ == bstack1l1lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ⏙"):
        bstack11l111ll1_opy_ = bstack1l1lll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⏚")
    bstack1l1ll111_opy_ = {
        bstack1l1lll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⏛"): bstack11l111ll1_opy_,
        bstack1l1lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ⏜"): bstack1l1l111l_opy_
    }
    bstack1l11ll1l_opy_.bstack1lll1111_opy_(bstack1l1ll111_opy_)
    if bstack11l111ll1_opy_ == bstack1l1lll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⏝"):
        threading.current_thread().bstackTestMeta = {bstack1l1lll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⏞"): bstack1l1lll1_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ⏟")}
    elif bstack11l111ll1_opy_ == bstack1l1lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⏠"):
        threading.current_thread().bstackTestMeta = {bstack1l1lll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⏡"): getattr(result, bstack1l1lll1_opy_ (u"ࠩࡲࡹࡹࡩ࡯࡮ࡧࠪ⏢"), bstack1l1lll1_opy_ (u"ࠪࠫ⏣"))}
def bstack1lll1lllll1l_opy_(test, bstack1l11l1ll_opy_, bstack11l111ll1_opy_, result=None, call=None, outcome=None, bstack1lll1lll1l1l_opy_=None):
    logger.debug(bstack1l1lll1_opy_ (u"ࠫࡸ࡫࡮ࡥࡡ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡨࡰࡱ࡮ࠤࡩࡧࡴࡢ࠮ࠣࡩࡻ࡫࡮ࡵࡖࡼࡴࡪࠦ࠭ࠡࡽࢀࠫ⏤").format(bstack11l111ll1_opy_))
    hook_data = bstack1lll1llll1ll_opy_(test, bstack1l11l1ll_opy_, bstack11l111ll1_opy_, result, call, outcome, bstack1lll1lll1l1l_opy_)
    bstack1l1ll111_opy_ = {
        bstack1l1lll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⏥"): bstack11l111ll1_opy_,
        bstack1l1lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨ⏦"): hook_data
    }
    bstack1l11ll1l_opy_.bstack1lll1111_opy_(bstack1l1ll111_opy_)
def bstack1l1l1l11_opy_(bstack1l11l1ll_opy_):
    if not bstack1l11l1ll_opy_:
        return None
    if bstack1l11l1ll_opy_.get(bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ⏧"), None):
        return getattr(bstack1l11l1ll_opy_[bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ⏨")], bstack1l1lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⏩"), None)
    return bstack1l11l1ll_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⏪"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.LOG, bstack1lll1lll11l_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_.LOG, bstack1lll1lll11l_opy_.POST, request, caplog)
        return # skip all existing operations
    try:
        if not bstack1l11ll1l_opy_.on():
            return
        places = [bstack1l1lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ⏫"), bstack1l1lll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ⏬"), bstack1l1lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ⏭")]
        logs = []
        for bstack1lll1llllll1_opy_ in places:
            records = caplog.get_records(bstack1lll1llllll1_opy_)
            bstack1lll1ll11lll_opy_ = bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⏮") if bstack1lll1llllll1_opy_ == bstack1l1lll1_opy_ (u"ࠨࡥࡤࡰࡱ࠭⏯") else bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⏰")
            bstack1lll1lllll11_opy_ = request.node.nodeid + (bstack1l1lll1_opy_ (u"ࠪࠫ⏱") if bstack1lll1llllll1_opy_ == bstack1l1lll1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ⏲") else bstack1l1lll1_opy_ (u"ࠬ࠳ࠧ⏳") + bstack1lll1llllll1_opy_)
            test_uuid = bstack1l1l1l11_opy_(_1l11l1l1_opy_.get(bstack1lll1lllll11_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack1111ll1l1l1_opy_(record.message):
                    continue
                logs.append({
                    bstack1l1lll1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⏴"): bstack1111l1l1l11_opy_(record.created).isoformat() + bstack1l1lll1_opy_ (u"࡛ࠧࠩ⏵"),
                    bstack1l1lll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ⏶"): record.levelname,
                    bstack1l1lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⏷"): record.message,
                    bstack1lll1ll11lll_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1l11ll1l_opy_.bstack1l1l1111_opy_(logs)
    except Exception as err:
        print(bstack1l1lll1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡨࡵ࡮ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧ࠽ࠤࢀࢃࠧ⏸"), str(err))
def bstack1l1l111l11_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack111lllll1_opy_
    bstack1llll11111_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ⏹"), None) and bstack1l1l1l1l_opy_(
            threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ⏺"), None)
    bstack11l1111ll1_opy_ = getattr(driver, bstack1l1lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭⏻"), None) != None and getattr(driver, bstack1l1lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ⏼"), None) == True
    if sequence == bstack1l1lll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ⏽") and driver != None:
      if not bstack111lllll1_opy_ and bstack1llll1111ll_opy_() and bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⏾") in CONFIG and CONFIG[bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⏿")] == True and bstack1l11111ll_opy_.bstack111l11l1l1_opy_(driver_command) and (bstack11l1111ll1_opy_ or bstack1llll11111_opy_) and not bstack11111111l_opy_(args):
        try:
          bstack111lllll1_opy_ = True
          logger.debug(bstack1l1lll1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡿࢂ࠭␀").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack1l1lll1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡶࡧࡦࡴࠠࡼࡿࠪ␁").format(str(err)))
        bstack111lllll1_opy_ = False
    if sequence == bstack1l1lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ␂"):
        if driver_command == bstack1l1lll1_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫ␃"):
            bstack1l11ll1l_opy_.bstack1l111ll11_opy_({
                bstack1l1lll1_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ␄"): response[bstack1l1lll1_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ␅")],
                bstack1l1lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ␆"): store[bstack1l1lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ␇")]
            })
def bstack1l11ll11l1_opy_():
    global bstack1l11l1111l_opy_
    bstack111l11l1l_opy_.bstack1l1l11l111_opy_()
    logging.shutdown()
    bstack1l11ll1l_opy_.bstack1ll11lll_opy_()
    for driver in bstack1l11l1111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1ll1l1l1_opy_(*args):
    global bstack1l11l1111l_opy_
    bstack1l11ll1l_opy_.bstack1ll11lll_opy_()
    for driver in bstack1l11l1111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l1111ll11_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack11l1l1lll1_opy_(self, *args, **kwargs):
    bstack1ll1111l1l_opy_ = bstack1l111ll111_opy_(self, *args, **kwargs)
    bstack111l1llll_opy_ = getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭␈"), None)
    if bstack111l1llll_opy_ and bstack111l1llll_opy_.get(bstack1l1lll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭␉"), bstack1l1lll1_opy_ (u"ࠧࠨ␊")) == bstack1l1lll1_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ␋"):
        bstack1l11ll1l_opy_.bstack111l111l1_opy_(self)
    return bstack1ll1111l1l_opy_
@measure(event_name=EVENTS.bstack1l1lll1lll_opy_, stage=STAGE.bstack111ll111l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1l11ll1ll1_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
    if bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭␌")):
        return
    bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧ␍"), True)
    global bstack1l1ll111l1_opy_
    global bstack1l11l111l_opy_
    bstack1l1ll111l1_opy_ = framework_name
    logger.info(bstack1ll11l11l1_opy_.format(bstack1l1ll111l1_opy_.split(bstack1l1lll1_opy_ (u"ࠫ࠲࠭␎"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1llll1111ll_opy_():
            Service.start = bstack11l11ll1ll_opy_
            Service.stop = bstack1l11lll11_opy_
            webdriver.Remote.get = bstack1l1l1lll11_opy_
            webdriver.Remote.__init__ = bstack11111lll1l_opy_
            if not isinstance(os.getenv(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭␏")), str):
                return
            WebDriver.quit = bstack1l1ll1ll1_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1l11ll1l_opy_.on():
            webdriver.Remote.__init__ = bstack11l1l1lll1_opy_
        bstack1l11l111l_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫ␐")):
        bstack1l11l111l_opy_ = eval(os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬ␑")))
    if not bstack1l11l111l_opy_:
        bstack1ll1ll1ll1_opy_(bstack1l1lll1_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥ␒"), bstack1l1111lll1_opy_)
    if bstack1l1l1llll_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack1l1lll1_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ␓")) and callable(getattr(RemoteConnection, bstack1l1lll1_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ␔"))):
                RemoteConnection._get_proxy_url = bstack111l11lll_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack111l11lll_opy_
        except Exception as e:
            logger.error(bstack11111l11l1_opy_.format(str(e)))
    if bstack1l1lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ␕") in str(framework_name).lower():
        if not bstack1llll1111ll_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1lll1ll111_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11l1l1ll11_opy_
            Config.getoption = bstack11l1l1ll1l_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1ll111l1l_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11lll1l11l_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1l1ll1ll1_opy_(self):
    global bstack1l1ll111l1_opy_
    global bstack11ll11111_opy_
    global bstack11ll11lll1_opy_
    try:
        if bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ␖") in bstack1l1ll111l1_opy_ and self.session_id != None and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪ␗"), bstack1l1lll1_opy_ (u"ࠧࠨ␘")) != bstack1l1lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ␙"):
            bstack11ll1lll11_opy_ = bstack1l1lll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ␚") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l1lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ␛")
            bstack1l111llll1_opy_(logger, True)
            if os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧ␜"), None):
                self.execute_script(
                    bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪ␝") + json.dumps(
                        os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ␞"))) + bstack1l1lll1_opy_ (u"ࠧࡾࡿࠪ␟"))
            if self != None:
                bstack111lll1111_opy_(self, bstack11ll1lll11_opy_, bstack1l1lll1_opy_ (u"ࠨ࠮ࠣࠫ␠").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1l1l111111l_opy_(bstack1l1l1l1ll1l_opy_):
            item = store.get(bstack1l1lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭␡"), None)
            if item is not None and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ␢"), None):
                bstack11l11ll1_opy_.bstack1llllllll_opy_(self, bstack1ll1l1l1l_opy_, logger, item)
        threading.current_thread().testStatus = bstack1l1lll1_opy_ (u"ࠫࠬ␣")
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨ␤") + str(e))
    bstack11ll11lll1_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1l1lllll11_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack11111lll1l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack11ll11111_opy_
    global bstack1lll111l11_opy_
    global bstack11lll1111l_opy_
    global bstack1l1ll111l1_opy_
    global bstack1l111ll111_opy_
    global bstack1l11l1111l_opy_
    global bstack1l111lllll_opy_
    global bstack1111l11l1_opy_
    global bstack1ll1l1l1l_opy_
    CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ␥")] = str(bstack1l1ll111l1_opy_) + str(__version__)
    command_executor = bstack111ll1ll1l_opy_(bstack1l111lllll_opy_, CONFIG)
    logger.debug(bstack11l1l111ll_opy_.format(command_executor))
    proxy = bstack11l111ll11_opy_(CONFIG, proxy)
    bstack1l11l1lll_opy_ = 0
    try:
        if bstack11lll1111l_opy_ is True:
            bstack1l11l1lll_opy_ = int(os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ␦")))
    except:
        bstack1l11l1lll_opy_ = 0
    bstack1l1l11111_opy_ = bstack1lll11l1l1_opy_(CONFIG, bstack1l11l1lll_opy_)
    logger.debug(bstack1llll1lll1_opy_.format(str(bstack1l1l11111_opy_)))
    bstack1ll1l1l1l_opy_ = CONFIG.get(bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ␧"))[bstack1l11l1lll_opy_]
    if bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭␨") in CONFIG and CONFIG[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ␩")]:
        bstack11llll1111_opy_(bstack1l1l11111_opy_, bstack1111l11l1_opy_)
    if bstack1lll1ll1l_opy_.bstack11lll1lll_opy_(CONFIG, bstack1l11l1lll_opy_) and bstack1lll1ll1l_opy_.bstack1l11ll1l11_opy_(bstack1l1l11111_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1l1l111111l_opy_(bstack1l1l1l1ll1l_opy_):
            bstack1lll1ll1l_opy_.set_capabilities(bstack1l1l11111_opy_, CONFIG)
    if desired_capabilities:
        bstack1l1l11lll1_opy_ = bstack11l1l1llll_opy_(desired_capabilities)
        bstack1l1l11lll1_opy_[bstack1l1lll1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ␪")] = bstack1111lll1l1_opy_(CONFIG)
        bstack1l1ll11lll_opy_ = bstack1lll11l1l1_opy_(bstack1l1l11lll1_opy_)
        if bstack1l1ll11lll_opy_:
            bstack1l1l11111_opy_ = update(bstack1l1ll11lll_opy_, bstack1l1l11111_opy_)
        desired_capabilities = None
    if options:
        bstack111l1l11l_opy_(options, bstack1l1l11111_opy_)
    if not options:
        options = bstack11ll11l111_opy_(bstack1l1l11111_opy_)
    if proxy and bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ␫")):
        options.proxy(proxy)
    if options and bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ␬")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1ll1ll11ll_opy_() < version.parse(bstack1l1lll1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭␭")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1l1l11111_opy_)
    logger.info(bstack1lllll1lll_opy_)
    bstack11l1l1111l_opy_.end(EVENTS.bstack1l1lll1lll_opy_.value, EVENTS.bstack1l1lll1lll_opy_.value + bstack1l1lll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ␮"),
                               EVENTS.bstack1l1lll1lll_opy_.value + bstack1l1lll1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ␯"), True, None)
    try:
        if bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ␰")):
            bstack1l111ll111_opy_(self, command_executor=command_executor,
                      options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
        elif bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ␱")):
            bstack1l111ll111_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities, options=options,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        elif bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬ␲")):
            bstack1l111ll111_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        else:
            bstack1l111ll111_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive)
    except Exception as bstack11111l1lll_opy_:
        logger.error(bstack111l1l1lll_opy_.format(bstack1l1lll1_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠬ␳"), str(bstack11111l1lll_opy_)))
        raise bstack11111l1lll_opy_
    try:
        bstack1lll1l1ll1_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨ␴")
        if bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࡢ࠲ࠩ␵")):
            bstack1lll1l1ll1_opy_ = self.caps.get(bstack1l1lll1_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ␶"))
        else:
            bstack1lll1l1ll1_opy_ = self.capabilities.get(bstack1l1lll1_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥ␷"))
        if bstack1lll1l1ll1_opy_:
            bstack11ll1l11ll_opy_(bstack1lll1l1ll1_opy_)
            if bstack1ll1ll11ll_opy_() <= version.parse(bstack1l1lll1_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫ␸")):
                self.command_executor._url = bstack1l1lll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ␹") + bstack1l111lllll_opy_ + bstack1l1lll1_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥ␺")
            else:
                self.command_executor._url = bstack1l1lll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤ␻") + bstack1lll1l1ll1_opy_ + bstack1l1lll1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤ␼")
            logger.debug(bstack1111l1lll1_opy_.format(bstack1lll1l1ll1_opy_))
        else:
            logger.debug(bstack1lll111ll1_opy_.format(bstack1l1lll1_opy_ (u"ࠤࡒࡴࡹ࡯࡭ࡢ࡮ࠣࡌࡺࡨࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥ␽")))
    except Exception as e:
        logger.debug(bstack1lll111ll1_opy_.format(e))
    bstack11ll11111_opy_ = self.session_id
    if bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ␾") in bstack1l1ll111l1_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack1l1lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ␿"), None)
        if item:
            bstack1lll1ll11ll1_opy_ = getattr(item, bstack1l1lll1_opy_ (u"ࠬࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࡡࡶࡸࡦࡸࡴࡦࡦࠪ⑀"), False)
            if not getattr(item, bstack1l1lll1_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧ⑁"), None) and bstack1lll1ll11ll1_opy_:
                setattr(store[bstack1l1lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⑂")], bstack1l1lll1_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ⑃"), self)
        bstack111l1llll_opy_ = getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪ⑄"), None)
        if bstack111l1llll_opy_ and bstack111l1llll_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ⑅"), bstack1l1lll1_opy_ (u"ࠫࠬ⑆")) == bstack1l1lll1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭⑇"):
            bstack1l11ll1l_opy_.bstack111l111l1_opy_(self)
    bstack1l11l1111l_opy_.append(self)
    if bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⑈") in CONFIG and bstack1l1lll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⑉") in CONFIG[bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ⑊")][bstack1l11l1lll_opy_]:
        bstack1lll111l11_opy_ = CONFIG[bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⑋")][bstack1l11l1lll_opy_][bstack1l1lll1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⑌")]
    logger.debug(bstack11111ll1l_opy_.format(bstack11ll11111_opy_))
@measure(event_name=EVENTS.bstack1ll1ll1111_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1l1l1lll11_opy_(self, url):
    global bstack11llll11l_opy_
    global CONFIG
    try:
        bstack11l1lll1l1_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack11llllllll_opy_.format(str(err)))
    try:
        bstack11llll11l_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack1l1ll11ll1_opy_):
                bstack11l1lll1l1_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack11llllllll_opy_.format(str(err)))
        raise e
def bstack1111ll11l_opy_(item, when):
    global bstack1l11111l11_opy_
    try:
        bstack1l11111l11_opy_(item, when)
    except Exception as e:
        pass
def bstack1ll111l1l_opy_(item, call, rep):
    global bstack111l1ll1l_opy_
    global bstack1l11l1111l_opy_
    name = bstack1l1lll1_opy_ (u"ࠫࠬ⑍")
    try:
        if rep.when == bstack1l1lll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ⑎"):
            bstack11ll11111_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack1l1lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⑏"))
            try:
                if (str(skipSessionName).lower() != bstack1l1lll1_opy_ (u"ࠧࡵࡴࡸࡩࠬ⑐")):
                    name = str(rep.nodeid)
                    bstack1lllll11ll_opy_ = bstack1l11llll1_opy_(bstack1l1lll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⑑"), name, bstack1l1lll1_opy_ (u"ࠩࠪ⑒"), bstack1l1lll1_opy_ (u"ࠪࠫ⑓"), bstack1l1lll1_opy_ (u"ࠫࠬ⑔"), bstack1l1lll1_opy_ (u"ࠬ࠭⑕"))
                    os.environ[bstack1l1lll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ⑖")] = name
                    for driver in bstack1l11l1111l_opy_:
                        if bstack11ll11111_opy_ == driver.session_id:
                            driver.execute_script(bstack1lllll11ll_opy_)
            except Exception as e:
                logger.debug(bstack1l1lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ⑗").format(str(e)))
            try:
                bstack1ll1ll1ll_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack1l1lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ⑘"):
                    status = bstack1l1lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⑙") if rep.outcome.lower() == bstack1l1lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⑚") else bstack1l1lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ⑛")
                    reason = bstack1l1lll1_opy_ (u"ࠬ࠭⑜")
                    if status == bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭⑝"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack1l1lll1_opy_ (u"ࠧࡪࡰࡩࡳࠬ⑞") if status == bstack1l1lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⑟") else bstack1l1lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ①")
                    data = name + bstack1l1lll1_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬ②") if status == bstack1l1lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ③") else name + bstack1l1lll1_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩࠧࠠࠨ④") + reason
                    bstack111111111_opy_ = bstack1l11llll1_opy_(bstack1l1lll1_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ⑤"), bstack1l1lll1_opy_ (u"ࠧࠨ⑥"), bstack1l1lll1_opy_ (u"ࠨࠩ⑦"), bstack1l1lll1_opy_ (u"ࠩࠪ⑧"), level, data)
                    for driver in bstack1l11l1111l_opy_:
                        if bstack11ll11111_opy_ == driver.session_id:
                            driver.execute_script(bstack111111111_opy_)
            except Exception as e:
                logger.debug(bstack1l1lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤࡱࡱࡸࡪࡾࡴࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ⑨").format(str(e)))
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡤࡸࡪࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁࡽࠨ⑩").format(str(e)))
    bstack111l1ll1l_opy_(item, call, rep)
notset = Notset()
def bstack11l1l1ll1l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack111l1llll1_opy_
    if str(name).lower() == bstack1l1lll1_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬ⑪"):
        return bstack1l1lll1_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧ⑫")
    else:
        return bstack111l1llll1_opy_(self, name, default, skip)
def bstack111l11lll_opy_(self):
    global CONFIG
    global bstack11lllll1l1_opy_
    try:
        proxy = bstack11lll11ll_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack1l1lll1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ⑬")):
                proxies = bstack11l111llll_opy_(proxy, bstack111ll1ll1l_opy_())
                if len(proxies) > 0:
                    protocol, bstack11l1llll1l_opy_ = proxies.popitem()
                    if bstack1l1lll1_opy_ (u"ࠣ࠼࠲࠳ࠧ⑭") in bstack11l1llll1l_opy_:
                        return bstack11l1llll1l_opy_
                    else:
                        return bstack1l1lll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ⑮") + bstack11l1llll1l_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack1l1lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢ⑯").format(str(e)))
    return bstack11lllll1l1_opy_(self)
def bstack1l1l1llll_opy_():
    return (bstack1l1lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ⑰") in CONFIG or bstack1l1lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ⑱") in CONFIG) and bstack111l1l11ll_opy_() and bstack1ll1ll11ll_opy_() >= version.parse(
        bstack11ll1l1ll_opy_)
def bstack1llll1111l_opy_(self,
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
    global bstack1lll111l11_opy_
    global bstack11lll1111l_opy_
    global bstack1l1ll111l1_opy_
    CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ⑲")] = str(bstack1l1ll111l1_opy_) + str(__version__)
    bstack1l11l1lll_opy_ = 0
    try:
        if bstack11lll1111l_opy_ is True:
            bstack1l11l1lll_opy_ = int(os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ⑳")))
    except:
        bstack1l11l1lll_opy_ = 0
    CONFIG[bstack1l1lll1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ⑴")] = True
    bstack1l1l11111_opy_ = bstack1lll11l1l1_opy_(CONFIG, bstack1l11l1lll_opy_)
    logger.debug(bstack1llll1lll1_opy_.format(str(bstack1l1l11111_opy_)))
    if CONFIG.get(bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭⑵")):
        bstack11llll1111_opy_(bstack1l1l11111_opy_, bstack1111l11l1_opy_)
    if bstack1l1lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭⑶") in CONFIG and bstack1l1lll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⑷") in CONFIG[bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⑸")][bstack1l11l1lll_opy_]:
        bstack1lll111l11_opy_ = CONFIG[bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⑹")][bstack1l11l1lll_opy_][bstack1l1lll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⑺")]
    import urllib
    import json
    if bstack1l1lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⑻") in CONFIG and str(CONFIG[bstack1l1lll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⑼")]).lower() != bstack1l1lll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ⑽"):
        bstack111ll1ll11_opy_ = bstack111l1ll11_opy_()
        bstack111llll11_opy_ = bstack111ll1ll11_opy_ + urllib.parse.quote(json.dumps(bstack1l1l11111_opy_))
    else:
        bstack111llll11_opy_ = bstack1l1lll1_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭⑾") + urllib.parse.quote(json.dumps(bstack1l1l11111_opy_))
    browser = self.connect(bstack111llll11_opy_)
    return browser
def bstack111lll11l_opy_():
    global bstack1l11l111l_opy_
    global bstack1l1ll111l1_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11l1ll1lll_opy_
        if not bstack1llll1111ll_opy_():
            global bstack1l11llllll_opy_
            if not bstack1l11llllll_opy_:
                from bstack_utils.helper import bstack1111ll111l_opy_, bstack111l11llll_opy_
                bstack1l11llllll_opy_ = bstack1111ll111l_opy_()
                bstack111l11llll_opy_(bstack1l1ll111l1_opy_)
            BrowserType.connect = bstack11l1ll1lll_opy_
            return
        BrowserType.launch = bstack1llll1111l_opy_
        bstack1l11l111l_opy_ = True
    except Exception as e:
        pass
def bstack1lll1ll1111l_opy_():
    global CONFIG
    global bstack1l1lllllll_opy_
    global bstack1l111lllll_opy_
    global bstack1111l11l1_opy_
    global bstack11lll1111l_opy_
    global bstack1111ll1ll_opy_
    CONFIG = json.loads(os.environ.get(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࠫ⑿")))
    bstack1l1lllllll_opy_ = eval(os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ⒀")))
    bstack1l111lllll_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡈࡖࡄࡢ࡙ࡗࡒࠧ⒁"))
    bstack111lll1ll_opy_(CONFIG, bstack1l1lllllll_opy_)
    bstack1111ll1ll_opy_ = bstack111l11l1l_opy_.configure_logger(CONFIG, bstack1111ll1ll_opy_)
    if cli.bstack11lll11lll_opy_():
        bstack1llll111ll_opy_.invoke(Events.CONNECT, bstack1lll1l1l1l_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ⒂"), bstack1l1lll1_opy_ (u"ࠩ࠳ࠫ⒃")))
        cli.bstack1l1l11l11ll_opy_(cli_context.platform_index)
        cli.bstack1l1l11l1l1l_opy_(bstack111ll1ll1l_opy_(bstack1l111lllll_opy_, CONFIG), cli_context.platform_index, bstack11ll11l111_opy_)
        cli.bstack1l1l1ll111l_opy_()
        logger.debug(bstack1l1lll1_opy_ (u"ࠥࡇࡑࡏࠠࡪࡵࠣࡥࡨࡺࡩࡷࡧࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤ⒄") + str(cli_context.platform_index) + bstack1l1lll1_opy_ (u"ࠦࠧ⒅"))
        return # skip all existing operations
    global bstack1l111ll111_opy_
    global bstack11ll11lll1_opy_
    global bstack1l1l11l1ll_opy_
    global bstack11ll111111_opy_
    global bstack11l1ll1111_opy_
    global bstack1l1ll1111_opy_
    global bstack1l111111ll_opy_
    global bstack11llll11l_opy_
    global bstack11lllll1l1_opy_
    global bstack111l1llll1_opy_
    global bstack1l11111l11_opy_
    global bstack111l1ll1l_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1l111ll111_opy_ = webdriver.Remote.__init__
        bstack11ll11lll1_opy_ = WebDriver.quit
        bstack1l111111ll_opy_ = WebDriver.close
        bstack11llll11l_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack1l1lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ⒆") in CONFIG or bstack1l1lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ⒇") in CONFIG) and bstack111l1l11ll_opy_():
        if bstack1ll1ll11ll_opy_() < version.parse(bstack11ll1l1ll_opy_):
            logger.error(bstack1ll1l1l11_opy_.format(bstack1ll1ll11ll_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack1l1lll1_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ⒈")) and callable(getattr(RemoteConnection, bstack1l1lll1_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ⒉"))):
                    bstack11lllll1l1_opy_ = RemoteConnection._get_proxy_url
                else:
                    from selenium.webdriver.remote.client_config import ClientConfig
                    bstack11lllll1l1_opy_ = ClientConfig.get_proxy_url
            except Exception as e:
                logger.error(bstack11111l11l1_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack111l1llll1_opy_ = Config.getoption
        from _pytest import runner
        bstack1l11111l11_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack11l11l11_opy_)
    try:
        from pytest_bdd import reporting
        bstack111l1ll1l_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ⒊"))
    bstack1111l11l1_opy_ = CONFIG.get(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ⒋"), {}).get(bstack1l1lll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭⒌"))
    bstack11lll1111l_opy_ = True
    bstack1l11ll1ll1_opy_(bstack1111lllll1_opy_)
if (bstack1111ll11111_opy_()):
    bstack1lll1ll1111l_opy_()
@error_handler(class_method=False)
def bstack1lll1lll11l1_opy_(hook_name, event, bstack1ll1l1111l1_opy_=None):
    if hook_name not in [bstack1l1lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭⒍"), bstack1l1lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪ⒎"), bstack1l1lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭⒏"), bstack1l1lll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ⒐"), bstack1l1lll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ⒑"), bstack1l1lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ⒒"), bstack1l1lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪ⒓"), bstack1l1lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧ⒔")]:
        return
    node = store[bstack1l1lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⒕")]
    if hook_name in [bstack1l1lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭⒖"), bstack1l1lll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ⒗")]:
        node = store[bstack1l1lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡱࡴࡪࡵ࡭ࡧࡢ࡭ࡹ࡫࡭ࠨ⒘")]
    elif hook_name in [bstack1l1lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ⒙"), bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬ⒚")]:
        node = store[bstack1l1lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪ⒛")]
    hook_type = bstack11l11l111l1_opy_(hook_name)
    if event == bstack1l1lll1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭⒜"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_[hook_type], bstack1lll1lll11l_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack1llll11l_opy_ = {
            bstack1l1lll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⒝"): uuid,
            bstack1l1lll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⒞"): bstack1ll1llll_opy_(),
            bstack1l1lll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⒟"): bstack1l1lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ⒠"),
            bstack1l1lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ⒡"): hook_type,
            bstack1l1lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨ⒢"): hook_name
        }
        store[bstack1l1lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⒣")].append(uuid)
        bstack1lll1lll1111_opy_ = node.nodeid
        if hook_type == bstack1l1lll1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬ⒤"):
            if not _1l11l1l1_opy_.get(bstack1lll1lll1111_opy_, None):
                _1l11l1l1_opy_[bstack1lll1lll1111_opy_] = {bstack1l1lll1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⒥"): []}
            _1l11l1l1_opy_[bstack1lll1lll1111_opy_][bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⒦")].append(bstack1llll11l_opy_[bstack1l1lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⒧")])
        _1l11l1l1_opy_[bstack1lll1lll1111_opy_ + bstack1l1lll1_opy_ (u"ࠫ࠲࠭⒨") + hook_name] = bstack1llll11l_opy_
        bstack1lll1lllll1l_opy_(node, bstack1llll11l_opy_, bstack1l1lll1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⒩"))
    elif event == bstack1l1lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ⒪"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11ll_opy_[hook_type], bstack1lll1lll11l_opy_.POST, node, None, bstack1ll1l1111l1_opy_)
            return
        bstack1ll11l1l_opy_ = node.nodeid + bstack1l1lll1_opy_ (u"ࠧ࠮ࠩ⒫") + hook_name
        _1l11l1l1_opy_[bstack1ll11l1l_opy_][bstack1l1lll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⒬")] = bstack1ll1llll_opy_()
        bstack1lll1lll11ll_opy_(_1l11l1l1_opy_[bstack1ll11l1l_opy_][bstack1l1lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⒭")])
        bstack1lll1lllll1l_opy_(node, _1l11l1l1_opy_[bstack1ll11l1l_opy_], bstack1l1lll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⒮"), bstack1lll1lll1l1l_opy_=bstack1ll1l1111l1_opy_)
def bstack1lll1lll1l11_opy_():
    global bstack1llll1111l1l_opy_
    if bstack1l1l1lll1_opy_():
        bstack1llll1111l1l_opy_ = bstack1l1lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨ⒯")
    else:
        bstack1llll1111l1l_opy_ = bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ⒰")
def pytest_collection_modifyitems(session, config, items):
    bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡆࡪ࡮ࡷࡩࡷࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦࠣࡴࡾࡺࡥࡴࡶࠣ࡭ࡹ࡫࡭ࡴࠢࡥࡥࡸ࡫ࡤࠡࡱࡱࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡦࡦࠣࡷࡪࡲࡥࡤࡶࡲࡶࡸࠦࡦࡳࡱࡰࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸ࡫ࡲࡷࡧࡵ࠲ࠏࠦࠠࠡࠢࠥࠦࠧ⒱")
    import os
    bstack1lll1ll11l11_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡏࡓࡅࡋࡉࡘ࡚ࡒࡂࡖࡈࡈࡤ࡙ࡅࡍࡇࡆࡘࡔࡘࡓࠨ⒲"))
    if not bstack1lll1ll11l11_opy_:
        return
    try:
        bstack1llll111111l_opy_ = json.loads(bstack1lll1ll11l11_opy_)
        if not isinstance(bstack1llll111111l_opy_, (list, set)) or not bstack1llll111111l_opy_:
            return
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠣࡅࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡵࡧࡲࡴࡧࠣࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡒࡖࡈࡎࡅࡔࡖࡕࡅ࡙ࡋࡄࡠࡕࡈࡐࡊࡉࡔࡐࡔࡖ࠾ࠥࠨ⒳") + str(e) + bstack1l1lll1_opy_ (u"ࠤࠥ⒴"))
        return
    selected = []
    deselected = []
    bstack1llll1111111_opy_ = set()
    for selector in bstack1llll111111l_opy_:
        if not selector or not isinstance(selector, str):
            continue
        bstack1llll1111111_opy_.add(selector)
    for item in items:
        nodeid = getattr(item, bstack1l1lll1_opy_ (u"ࠪࡲࡴࡪࡥࡪࡦࠪ⒵"), None)
        if not nodeid:
            deselected.append(item)
            continue
        if (
            nodeid in bstack1llll1111111_opy_ or
            any(sel in nodeid for sel in bstack1llll1111111_opy_)
        ):
            selected.append(item)
        else:
            deselected.append(item)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected
def pytest_collection_finish(session):
    bstack1l1lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡈࡧ࡬࡭ࡧࡧࠤࡦ࡬ࡴࡦࡴࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡪࡨࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡭࡮ࡨࡧࡹ࠳࡮ࡰࡦࡨ࡭ࡩࡹࠠࡧ࡮ࡤ࡫ࠥ࡯ࡳࠡࡷࡶࡩࡩ࠴ࠊࠡࠢࠣࠤࡕࡸࡩ࡯ࡶࡶࠤࡳࡵࡤࡦ࡫ࡧࡷࠥࡩ࡬ࡦࡣࡱࡰࡾࠦࡡ࡯ࡦࠣࡩࡽ࡯ࡴࡴࠢࡳࡽࡹ࡫ࡳࡵࠢ࡬ࡲࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࠯ࡲࡲࡱࡿࠠ࡮ࡱࡧࡩ࠳ࠐࠠࠡࠢࠣࠦࠧࠨⒶ")
    try:
        bstack1llll11111l1_opy_ = session.config.getoption(bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡩ࡯࡭࡮ࡨࡧࡹࡥ࡮ࡰࡦࡨ࡭ࡩࡹࠧⒷ"), False)
        if not bstack1llll11111l1_opy_:
            return
        bstack1lll1ll1lll1_opy_ = session.items
        bstack1llll1111ll1_opy_ = [item.nodeid for item in bstack1lll1ll1lll1_opy_]
        if bstack1llll1111ll1_opy_:
            print(bstack1l1lll1_opy_ (u"ࠨ࡜࡯ࠤⒸ").join(bstack1llll1111ll1_opy_))
            print(bstack1lll1ll1l11_opy_ (u"ࠢ࡝ࡰࡾࡰࡪࡴࠨ࡯ࡱࡧࡩ࡮ࡪࡳࠪࡿࠣࡸࡪࡹࡴࡴࠢࡦࡳࡱࡲࡥࡤࡶࡨࡨࠧⒹ"))
        else:
            print(bstack1l1lll1_opy_ (u"ࠣࡐࡲࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠨⒺ"))
        session.config.option.bstack1llll111l1l1_opy_ = True
    except Exception as e:
        logger.error(bstack1l1lll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡧࡹࡴࡢࡥ࡮ࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠻ࠢࠥⒻ") + str(e) + bstack1l1lll1_opy_ (u"ࠥࠦⒼ"))
def get_test_count_and_files(bstack111l11ll_opy_=None, bstack11l111ll_opy_=None, bstack1llll1lll_opy_=False):
    bstack1l1lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡕࡸ࡯ࡨࡴࡤࡱࡲࡧࡴࡪࡥࡤࡰࡱࡿࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡲࡼࡸࡪࡹࡴࠡࡶࡨࡷࡹࡹࠠࡸ࡫ࡷ࡬ࡴࡻࡴࠡࡵࡸࡦࡵࡸ࡯ࡤࡧࡶࡷ࠳ࠐࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡸࡪࡹࡴࡠࡣࡵ࡫ࡸࠦࠨ࡭࡫ࡶࡸ࠱ࠦ࡯ࡱࡶ࡬ࡳࡳࡧ࡬ࠪ࠼ࠣࡇࡴࡳࡰ࡭ࡧࡷࡩࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡰࡺࡶࡨࡷࡹࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴࠢ࡬ࡲࡨࡲࡵࡥ࡫ࡱ࡫ࠥࡶࡡࡵࡪࡶࠤࡦࡴࡤࠡࡨ࡯ࡥ࡬ࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡖࡤ࡯ࡪࡹࠠࡱࡴࡨࡧࡪࡪࡥ࡯ࡥࡨࠤࡴࡼࡥࡳࠢࡷࡩࡸࡺ࡟ࡱࡣࡷ࡬ࡸࠦࡩࡧࠢࡥࡳࡹ࡮ࠠࡢࡴࡨࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡶࡨࡷࡹࡥࡰࡢࡶ࡫ࡷࠥ࠮࡬ࡪࡵࡷࠤࡴࡸࠠࡴࡶࡵ࠰ࠥࡵࡰࡵ࡫ࡲࡲࡦࡲࠩ࠻ࠢࡗࡩࡸࡺࠠࡧ࡫࡯ࡩ࠭ࡹࠩ࠰ࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠬ࡮࡫ࡳࠪࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡦࡳࡱࡰ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡃࡢࡰࠣࡦࡪࠦࡡࠡࡵ࡬ࡲ࡬ࡲࡥࠡࡲࡤࡸ࡭ࠦࡳࡵࡴ࡬ࡲ࡬ࠦ࡯ࡳࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡦࡺࡨࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡎ࡭࡮ࡰࡴࡨࡨࠥ࡯ࡦࠡࡶࡨࡷࡹࡥࡡࡳࡩࡶࠤ࡮ࡹࠠࡱࡴࡲࡺ࡮ࡪࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡸ࡯࡬ࡦࡰࡷࠤ࠭ࡨ࡯ࡰ࡮࠯ࠤࡴࡶࡴࡪࡱࡱࡥࡱ࠯࠺ࠡࡋࡩࠤ࡙ࡸࡵࡦ࠮ࠣࡷࡺࡶࡰࡳࡧࡶࡷࡪࡹࠠࡱࡴ࡬ࡲࡹࠦ࡯ࡶࡶࡳࡹࡹ࠴ࠠࡅࡧࡩࡥࡺࡲࡴࠡࡈࡤࡰࡸ࡫࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࡦ࡬ࡧࡹࡀࠠࡄࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡩࡵࡪࠣࡲࡴࡪࡥࡪࡦࡶ࠰ࠥࡩ࡯ࡶࡰࡷ࠰ࠥࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴࠌࠣࠤࠥࠦࡅࡹࡣࡰࡴࡱ࡫ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡂࠦࡣࡰ࡮࡯ࡩࡨࡺ࡟ࡵࡧࡶࡸࡸࡥࡰࡳࡱࡪࡶࡦࡳ࡭ࡢࡶ࡬ࡧࡦࡲ࡬ࡺࠪࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡨࡷࡹࡥࡡࡳࡩࡶࡁࡠࠨࡴࡦࡵࡷࡷ࠴ࠨࠬࠡࠤ࠰ࡴࠧ࠲ࠠࠣࡲࡼࡸࡪࡹࡴࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡰ࡭ࡷࡪ࡭ࡳࠨࠬࠡࠤ࠰࠱ࡩࡸࡩࡷࡧࡵࠦ࠱ࠦࠢࡤࡪࡵࡳࡲ࡫ࠢ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡲࡦࡵࡸࡰࡹࡹࠠ࠾ࠢࡦࡳࡱࡲࡥࡤࡶࡢࡸࡪࡹࡴࡴࡡࡳࡶࡴ࡭ࡲࡢ࡯ࡰࡥࡹ࡯ࡣࡢ࡮࡯ࡽ࠭ࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴ࠿࡞ࠦࡘࡊࡋ࠰ࠤ࠯ࠤࠧࡺࡥࡴࡶࡶ࠳࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯࠱ࠥࡡ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡶࡹࡱࡺࡳࠡ࠿ࠣࡧࡴࡲ࡬ࡦࡥࡷࡣࡹ࡫ࡳࡵࡵࡢࡴࡷࡵࡧࡳࡣࡰࡱࡦࡺࡩࡤࡣ࡯ࡰࡾ࠮ࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࡀࠦࡘࡊࡋ࠰ࠤࠬࠎࠥࠦࠠࠡࠤࠥࠦⒽ")
    try:
        import pytest
        if bstack111l11ll_opy_ is not None:
            args = bstack111l11ll_opy_
        elif bstack11l111ll_opy_ is not None:
            if isinstance(bstack11l111ll_opy_, str):
                args = [bstack11l111ll_opy_]
            elif isinstance(bstack11l111ll_opy_, list):
                args = bstack11l111ll_opy_
            else:
                args = [bstack1l1lll1_opy_ (u"ࠧ࠴ࠢⒾ")]
        else:
            args = [bstack1l1lll1_opy_ (u"ࠨ࠮ࠣⒿ")]
        bstack1lll1ll1l11l_opy_ = list(args) + [bstack1l1lll1_opy_ (u"ࠢ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠣⓀ")]
        if bstack1llll1lll_opy_:
            bstack1lll1ll1l11l_opy_.extend([
                bstack1l1lll1_opy_ (u"ࠣ࠯࠰ࡵࡺ࡯ࡥࡵࠤⓁ"),
                bstack1l1lll1_opy_ (u"ࠤ࠰࠱ࡹࡨ࠽࡯ࡱࠥⓂ"),
                bstack1l1lll1_opy_ (u"ࠥ࠱ࡵࠨⓃ"), bstack1l1lll1_opy_ (u"ࠦࡳࡵ࠺ࡸࡣࡵࡲ࡮ࡴࡧࡴࠤⓄ"),
                bstack1l1lll1_opy_ (u"ࠧ࠳࠭࡯ࡱ࠰ࡷࡺࡳ࡭ࡢࡴࡼࠦⓅ")
            ])
        class bstack1lll1ll111ll_opy_:
            def __init__(self):
                self.collected = []
            def pytest_collection_finish(self, session):
                self.collected = [item.nodeid for item in session.items]
        bstack1llll1111lll_opy_ = bstack1lll1ll111ll_opy_()
        if bstack1llll1lll_opy_:
            import sys
            import io
            bstack1lll1ll1ll11_opy_ = sys.stdout
            bstack1lll1ll1l111_opy_ = sys.stderr
            sys.stdout = io.StringIO()
            sys.stderr = io.StringIO()
            try:
                pytest.main(bstack1lll1ll1l11l_opy_ + [bstack1l1lll1_opy_ (u"ࠨ࠭ࡱࠤⓆ"), bstack1l1lll1_opy_ (u"ࠢ࡯ࡱ࠽ࡧࡦࡩࡨࡦࡲࡵࡳࡻ࡯ࡤࡦࡴࠥⓇ")], plugins=[bstack1llll1111lll_opy_])
            finally:
                sys.stdout = bstack1lll1ll1ll11_opy_
                sys.stderr = bstack1lll1ll1l111_opy_
        else:
            pytest.main(bstack1lll1ll1l11l_opy_ + [bstack1l1lll1_opy_ (u"ࠣ࠯ࡳࠦⓈ"), bstack1l1lll1_opy_ (u"ࠤࡱࡳ࠿ࡩࡡࡤࡪࡨࡴࡷࡵࡶࡪࡦࡨࡶࠧⓉ")], plugins=[bstack1llll1111lll_opy_])
        bstack1llll1111ll1_opy_ = bstack1llll1111lll_opy_.collected
        test_files = set()
        for nodeid in bstack1llll1111ll1_opy_:
            if bstack1l1lll1_opy_ (u"ࠥ࠾࠿ࠨⓊ") in nodeid:
                file_path = nodeid.split(bstack1l1lll1_opy_ (u"ࠦ࠿ࡀࠢⓋ"), 1)[0]
                if file_path.endswith(bstack1l1lll1_opy_ (u"ࠬ࠴ࡰࡺࠩⓌ")):
                    test_files.add(file_path)
        result = {
            bstack1l1lll1_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹࠢⓍ"): True,
            bstack1l1lll1_opy_ (u"ࠢࡤࡱࡸࡲࡹࠨⓎ"): len(bstack1llll1111ll1_opy_),
            bstack1l1lll1_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࡴࠤⓏ"): bstack1llll1111ll1_opy_,
            bstack1l1lll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠨⓐ"): sorted(test_files)
        }
        if not bstack1llll1lll_opy_:
            logger.debug(bstack1l1lll1_opy_ (u"ࠥ࡟ࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࡞ࠢࡉࡳࡺࡴࡤࠡࡽࡵࡩࡸࡻ࡬ࡵ࡝ࠪࡧࡴࡻ࡮ࡵࠩࡠࢁࠥࡺࡥࡴࡶࡶࠤ࡮ࡴࠠࠣⓑ") + str(len(result[bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳࠨⓒ")])) + bstack1l1lll1_opy_ (u"ࠧࠦࡦࡪ࡮ࡨࡷࠧⓓ"))
        return result
    except Exception as e:
        logger.error(bstack1l1lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡵࡳ࡬ࡸࡡ࡮࡯ࡤࡸ࡮ࡩࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠾ࠥࠨⓔ") + str(e) + bstack1l1lll1_opy_ (u"ࠢࠣⓕ"))
        return {
            bstack1l1lll1_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴࠤⓖ"): False,
            bstack1l1lll1_opy_ (u"ࠤࡦࡳࡺࡴࡴࠣⓗ"): 0,
            bstack1l1lll1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࡶࠦⓘ"): [],
            bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳࠣⓙ"): []
        }
@bstack1l11ll1l_opy_.bstack1llll1l1lll1_opy_
def bstack1lll1ll1llll_opy_():
    bstack1lll1lll1l11_opy_()
    if cli.is_running():
        try:
            bstack11l1ll11l1l_opy_(bstack1lll1lll11l1_opy_)
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࡵࠣࡴࡦࡺࡣࡩ࠼ࠣࡿࢂࠨⓚ").format(e))
        return
    if bstack111l1l11ll_opy_():
        bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
        bstack1l1lll1_opy_ (u"࠭ࠧࠨࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡇࡱࡵࠤࡵࡶࡰࠡ࠿ࠣ࠵࠱ࠦ࡭ࡰࡦࡢࡩࡽ࡫ࡣࡶࡶࡨࠤ࡬࡫ࡴࡴࠢࡸࡷࡪࡪࠠࡧࡱࡵࠤࡦ࠷࠱ࡺࠢࡦࡳࡲࡳࡡ࡯ࡦࡶ࠱ࡼࡸࡡࡱࡲ࡬ࡲ࡬ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡲࡳࡴࠥࡄࠠ࠲࠮ࠣࡱࡴࡪ࡟ࡦࡺࡨࡧࡺࡺࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡣࡧࡦࡥࡺࡹࡥࠡ࡫ࡷࠤ࡮ࡹࠠࡱࡣࡷࡧ࡭࡫ࡤࠡ࡫ࡱࠤࡦࠦࡤࡪࡨࡩࡩࡷ࡫࡮ࡵࠢࡳࡶࡴࡩࡥࡴࡵࠣ࡭ࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡵࡴࠢࡺࡩࠥࡴࡥࡦࡦࠣࡸࡴࠦࡵࡴࡧࠣࡗࡪࡲࡥ࡯࡫ࡸࡱࡕࡧࡴࡤࡪࠫࡷࡪࡲࡥ࡯࡫ࡸࡱࡤ࡮ࡡ࡯ࡦ࡯ࡩࡷ࠯ࠠࡧࡱࡵࠤࡵࡶࡰࠡࡀࠣ࠵ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧࠨࠩⓛ")
        if bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫⓜ")):
            if CONFIG.get(bstack1l1lll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨⓝ")) is not None and int(CONFIG[bstack1l1lll1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩⓞ")]) > 1:
                bstack1lll1l111l_opy_(bstack1l1l111l11_opy_)
            return
        bstack1lll1l111l_opy_(bstack1l1l111l11_opy_)
    try:
        bstack11l1ll11l1l_opy_(bstack1lll1lll11l1_opy_)
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࡳࠡࡲࡤࡸࡨ࡮࠺ࠡࡽࢀࠦⓟ").format(e))
bstack1lll1ll1llll_opy_()