# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack1111l111l1_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11lllll111_opy_, bstack11llll1111_opy_, update, bstack1ll111lll1_opy_,
                                       bstack1111lll1l_opy_, bstack1ll11l1l11_opy_, bstack11111l1l1l_opy_, bstack11111llll1_opy_,
                                       bstack11ll11lll_opy_, bstack11l1l11l11_opy_, bstack1ll11l1l1_opy_,
                                       bstack1l11l1lll1_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1ll1ll111l_opy_)
from browserstack_sdk.bstack11111l1l_opy_ import bstack1lllllll1_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1l1l1llll1_opy_
from bstack_utils.capture import bstack1lll11ll_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack1ll11l1lll_opy_, bstack1ll1l1l111_opy_, bstack1l1ll1ll11_opy_, \
    bstack1ll11ll111_opy_
from bstack_utils.helper import bstack1lll111l_opy_, bstack111l1ll1ll1_opy_, bstack11lll1l1_opy_, bstack1111l1l11l_opy_, bstack1lll1l11111_opy_, bstack1l1111l1_opy_, \
    bstack1111lll11ll_opy_, \
    bstack1111ll1ll1l_opy_, bstack11lllll11l_opy_, bstack11lll1lll1_opy_, bstack111l11l1l11_opy_, bstack1lll1ll11l_opy_, Notset, \
    bstack1111ll1ll1_opy_, bstack111l111111l_opy_, bstack111l11lllll_opy_, Result, bstack1111l1ll1l1_opy_, bstack111l11l111l_opy_, error_handler, \
    bstack1l1111ll1_opy_, bstack1l11l11l1l_opy_, bstack11lllll1l1_opy_, bstack1111l11llll_opy_
from bstack_utils.bstack11l1ll1111l_opy_ import bstack11l1l1ll11l_opy_
from bstack_utils.messages import bstack111ll11111_opy_, bstack11ll1lll1_opy_, bstack1llll1l1ll_opy_, bstack1l1l11111_opy_, bstack111llll1_opy_, \
    bstack111l1l11ll_opy_, bstack1l1l1ll11_opy_, bstack11llll1ll1_opy_, bstack1111l1l1ll_opy_, bstack1l11l11lll_opy_, \
    bstack1l1lll11l_opy_, bstack1l11lllll_opy_, bstack11l111lll_opy_
from bstack_utils.proxy import bstack1l1l1l1ll_opy_, bstack1111llll1_opy_
from bstack_utils.bstack11ll11l1ll_opy_ import bstack11l111l1l1l_opy_, bstack11l111lll11_opy_, bstack11l111ll111_opy_, bstack11l111l1111_opy_, \
    bstack11l111ll1l1_opy_, bstack11l111l1ll1_opy_, bstack11l111ll11l_opy_, bstack1111lll111_opy_, bstack11l111l1lll_opy_
from bstack_utils.bstack111l11111l_opy_ import bstack111ll1ll1l_opy_
from bstack_utils.bstack1111ll1lll_opy_ import bstack11l111111l_opy_, bstack111l1l1lll_opy_, bstack11l11111l_opy_, \
    bstack1lllll1l1l_opy_, bstack1l1lll111l_opy_
from bstack_utils.bstack1l11l111_opy_ import bstack1ll11lll_opy_
from bstack_utils.bstack1lll11l1_opy_ import bstack1ll11l11_opy_
import bstack_utils.accessibility as bstack111ll11l_opy_
from bstack_utils.bstack11lllll1_opy_ import bstack1ll1l11l_opy_
from bstack_utils.bstack11ll1111l_opy_ import bstack11ll1111l_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack11111lll_opy_
from browserstack_sdk.__init__ import bstack1ll1ll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1l1l11ll1ll_opy_ import bstack1l1l111l111_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1ll1l_opy_ import bstack1l1l1ll1l_opy_, Events, bstack11lll1ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1ll111l11ll_opy_, bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l1l1ll1l_opy_ import bstack1l1l1ll1l_opy_, Events, bstack11lll1ll1_opy_
bstack1111lll1ll_opy_ = None
bstack1l1ll11ll1_opy_ = None
bstack1l1l11l1l1_opy_ = None
bstack1ll1ll1111_opy_ = None
bstack111llll1l_opy_ = None
bstack1l11l1l1ll_opy_ = None
bstack1l11llllll_opy_ = None
bstack1l11l1llll_opy_ = None
bstack11l11ll1ll_opy_ = None
bstack1l1ll1111l_opy_ = None
bstack11l111ll1_opy_ = None
bstack11lll111l_opy_ = None
bstack1l111111l_opy_ = None
bstack11lll1l11l_opy_ = bstack11lll1_opy_ (u"ࠫࠬ≱")
CONFIG = {}
bstack1ll1l11111_opy_ = False
bstack111111ll1l_opy_ = bstack11lll1_opy_ (u"ࠬ࠭≲")
bstack1l1111lll1_opy_ = bstack11lll1_opy_ (u"࠭ࠧ≳")
bstack1l1111111_opy_ = False
bstack1l1l11l11l_opy_ = []
bstack1l11ll1ll1_opy_ = bstack1ll11l1lll_opy_
bstack1lll1ll1ll11_opy_ = bstack11lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ≴")
bstack1l111l1l11_opy_ = {}
bstack1l11llll1_opy_ = None
bstack1111l11111_opy_ = False
logger = bstack1l1l1llll1_opy_.get_logger(__name__, bstack1l11ll1ll1_opy_)
store = {
    bstack11lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ≵"): []
}
bstack1lll1llllll1_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1l11l11l_opy_ = {}
current_test_uuid = None
cli_context = bstack1ll111l11ll_opy_(
    test_framework_name=bstack1111ll1111_opy_[bstack11lll1_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕ࠯ࡅࡈࡉ࠭≶")] if bstack1lll1ll11l_opy_() else bstack1111ll1111_opy_[bstack11lll1_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࠪ≷")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack111l1ll1l_opy_(page, bstack1l11lll11_opy_):
    try:
        page.evaluate(bstack11lll1_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧ≸"),
                      bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩ≹") + json.dumps(
                          bstack1l11lll11_opy_) + bstack11lll1_opy_ (u"ࠨࡽࡾࠤ≺"))
    except Exception as e:
        print(bstack11lll1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁࠧ≻"), e)
def bstack1111ll11ll_opy_(page, message, level):
    try:
        page.evaluate(bstack11lll1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ≼"), bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ≽") + json.dumps(
            message) + bstack11lll1_opy_ (u"ࠪ࠰ࠧࡲࡥࡷࡧ࡯ࠦ࠿࠭≾") + json.dumps(level) + bstack11lll1_opy_ (u"ࠫࢂࢃࠧ≿"))
    except Exception as e:
        print(bstack11lll1_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࢁࡽࠣ⊀"), e)
def pytest_configure(config):
    global bstack111111ll1l_opy_
    global CONFIG
    bstack1lll1l11l_opy_ = Config.bstack111ll1l1_opy_()
    config.args = bstack1ll11l11_opy_.bstack11l11l1111l_opy_(config.args)
    bstack1lll1l11l_opy_.bstack1ll1l11ll_opy_(bstack11lllll1l1_opy_(config.getoption(bstack11lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪ⊁"))))
    try:
        bstack1l1l1llll1_opy_.bstack11111ll111l_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack1l1l1ll1l_opy_.invoke(Events.CONNECT, bstack11lll1ll1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ⊂"), bstack11lll1_opy_ (u"ࠨ࠲ࠪ⊃")))
        config = json.loads(os.environ.get(bstack11lll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠣ⊄"), bstack11lll1_opy_ (u"ࠥࡿࢂࠨ⊅")))
        cli.bstack1l1l11111ll_opy_(bstack11lll1lll1_opy_(bstack111111ll1l_opy_, CONFIG), cli_context.platform_index, bstack1ll111lll1_opy_)
    if cli.bstack1l1l1llll1l_opy_(bstack1l1l111l111_opy_):
        cli.bstack1l1l11l1ll1_opy_()
        logger.debug(bstack11lll1_opy_ (u"ࠦࡈࡒࡉࠡ࡫ࡶࠤࡦࡩࡴࡪࡸࡨࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࠥ⊆") + str(cli_context.platform_index) + bstack11lll1_opy_ (u"ࠧࠨ⊇"))
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.BEFORE_ALL, bstack1llll11l111_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack11lll1_opy_ (u"ࠨࡷࡩࡧࡱࠦ⊈"), None)
    if cli.is_running() and when == bstack11lll1_opy_ (u"ࠢࡤࡣ࡯ࡰࠧ⊉"):
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.LOG_REPORT, bstack1llll11l111_opy_.PRE, item, call)
    outcome = yield
    if when == bstack11lll1_opy_ (u"ࠣࡥࡤࡰࡱࠨ⊊"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11lll1_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦ⊋")))
        if not passed:
            config = json.loads(os.environ.get(bstack11lll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠤ⊌"), bstack11lll1_opy_ (u"ࠦࢀࢃࠢ⊍")))
            if bstack11111lll_opy_.bstack11111111_opy_(config):
                bstack11111111lll_opy_ = bstack11111lll_opy_.bstack111l1l1l_opy_(config)
                if item.execution_count > bstack11111111lll_opy_:
                    print(bstack11lll1_opy_ (u"࡚ࠬࡥࡴࡶࠣࡪࡦ࡯࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡵࡩࡹࡸࡩࡦࡵ࠽ࠤࠬ⊎"), report.nodeid, os.environ.get(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ⊏")))
                    bstack11111lll_opy_.bstack111llllll1l_opy_(report.nodeid)
            else:
                print(bstack11lll1_opy_ (u"ࠧࡕࡧࡶࡸࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࠧ⊐"), report.nodeid, os.environ.get(bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭⊑")))
                bstack11111lll_opy_.bstack111llllll1l_opy_(report.nodeid)
        else:
            print(bstack11lll1_opy_ (u"ࠩࡗࡩࡸࡺࠠࡱࡣࡶࡷࡪࡪ࠺ࠡࠩ⊒"), report.nodeid, os.environ.get(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ⊓")))
    if cli.is_running():
        if when == bstack11lll1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥ⊔"):
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.BEFORE_EACH, bstack1llll11l111_opy_.POST, item, call, outcome)
        elif when == bstack11lll1_opy_ (u"ࠧࡩࡡ࡭࡮ࠥ⊕"):
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.LOG_REPORT, bstack1llll11l111_opy_.POST, item, call, outcome)
        elif when == bstack11lll1_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣ⊖"):
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.AFTER_EACH, bstack1llll11l111_opy_.POST, item, call, outcome)
        return # skip all existing operations
    skipSessionName = item.config.getoption(bstack11lll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⊗"))
    plugins = item.config.getoption(bstack11lll1_opy_ (u"ࠣࡲ࡯ࡹ࡬࡯࡮ࡴࠤ⊘"))
    report = outcome.get_result()
    os.environ[bstack11lll1_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬ⊙")] = report.nodeid
    bstack1lll1llll11l_opy_(item, call, report)
    if bstack11lll1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠣ⊚") not in plugins or bstack1lll1ll11l_opy_():
        return
    summary = []
    driver = getattr(item, bstack11lll1_opy_ (u"ࠦࡤࡪࡲࡪࡸࡨࡶࠧ⊛"), None)
    page = getattr(item, bstack11lll1_opy_ (u"ࠧࡥࡰࡢࡩࡨࠦ⊜"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1lll1ll11l11_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1lll1lll11ll_opy_(item, report, summary, skipSessionName)
def bstack1lll1ll11l11_opy_(item, report, summary, skipSessionName):
    if report.when == bstack11lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ⊝") and report.skipped:
        bstack11l111l1lll_opy_(report)
    if report.when in [bstack11lll1_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨ⊞"), bstack11lll1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥ⊟")]:
        return
    if not bstack1lll1l11111_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack11lll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⊠")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨ⊡") + json.dumps(
                    report.nodeid) + bstack11lll1_opy_ (u"ࠫࢂࢃࠧ⊢"))
        os.environ[bstack11lll1_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ⊣")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11lll1_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥ࠻ࠢࡾ࠴ࢂࠨ⊤").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11lll1_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤ⊥")))
    bstack1l11ll11ll_opy_ = bstack11lll1_opy_ (u"ࠣࠤ⊦")
    bstack11l111l1lll_opy_(report)
    if not passed:
        try:
            bstack1l11ll11ll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11lll1_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤ⊧").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l11ll11ll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11lll1_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧ⊨")))
        bstack1l11ll11ll_opy_ = bstack11lll1_opy_ (u"ࠦࠧ⊩")
        if not passed:
            try:
                bstack1l11ll11ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11lll1_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧ⊪").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l11ll11ll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡧࡥࡹࡧࠢ࠻ࠢࠪ⊫")
                    + json.dumps(bstack11lll1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠡࠣ⊬"))
                    + bstack11lll1_opy_ (u"ࠣ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࠦ⊭")
                )
            else:
                item._driver.execute_script(
                    bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡤࡢࡶࡤࠦ࠿ࠦࠧ⊮")
                    + json.dumps(str(bstack1l11ll11ll_opy_))
                    + bstack11lll1_opy_ (u"ࠥࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠨ⊯")
                )
        except Exception as e:
            summary.append(bstack11lll1_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡤࡲࡳࡵࡴࡢࡶࡨ࠾ࠥࢁ࠰ࡾࠤ⊰").format(e))
def bstack1lll1ll11lll_opy_(test_name, error_message):
    try:
        bstack1lll1ll1lll1_opy_ = []
        bstack1lll11ll11_opy_ = os.environ.get(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ⊱"), bstack11lll1_opy_ (u"࠭࠰ࠨ⊲"))
        bstack1l11ll1lll_opy_ = {bstack11lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⊳"): test_name, bstack11lll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ⊴"): error_message, bstack11lll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ⊵"): bstack1lll11ll11_opy_}
        bstack1lll1lll1l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11lll1_opy_ (u"ࠪࡴࡼࡥࡰࡺࡶࡨࡷࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ⊶"))
        if os.path.exists(bstack1lll1lll1l11_opy_):
            with open(bstack1lll1lll1l11_opy_) as f:
                bstack1lll1ll1lll1_opy_ = json.load(f)
        bstack1lll1ll1lll1_opy_.append(bstack1l11ll1lll_opy_)
        with open(bstack1lll1lll1l11_opy_, bstack11lll1_opy_ (u"ࠫࡼ࠭⊷")) as f:
            json.dump(bstack1lll1ll1lll1_opy_, f)
    except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡧࡵࡷ࡮ࡹࡴࡪࡰࡪࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡲࡼࡸࡪࡹࡴࠡࡧࡵࡶࡴࡸࡳ࠻ࠢࠪ⊸") + str(e))
def bstack1lll1lll11ll_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack11lll1_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧ⊹"), bstack11lll1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤ⊺")]:
        return
    if (str(skipSessionName).lower() != bstack11lll1_opy_ (u"ࠨࡶࡵࡹࡪ࠭⊻")):
        bstack111l1ll1l_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11lll1_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦ⊼")))
    bstack1l11ll11ll_opy_ = bstack11lll1_opy_ (u"ࠥࠦ⊽")
    bstack11l111l1lll_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l11ll11ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11lll1_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦ⊾").format(e)
                )
        try:
            if passed:
                bstack1l1lll111l_opy_(getattr(item, bstack11lll1_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫ⊿"), None), bstack11lll1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ⋀"))
            else:
                error_message = bstack11lll1_opy_ (u"ࠧࠨ⋁")
                if bstack1l11ll11ll_opy_:
                    bstack1111ll11ll_opy_(item._page, str(bstack1l11ll11ll_opy_), bstack11lll1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢ⋂"))
                    bstack1l1lll111l_opy_(getattr(item, bstack11lll1_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨ⋃"), None), bstack11lll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ⋄"), str(bstack1l11ll11ll_opy_))
                    error_message = str(bstack1l11ll11ll_opy_)
                else:
                    bstack1l1lll111l_opy_(getattr(item, bstack11lll1_opy_ (u"ࠫࡤࡶࡡࡨࡧࠪ⋅"), None), bstack11lll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ⋆"))
                bstack1lll1ll11lll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11lll1_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡺࡶࡤࡢࡶࡨࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻ࠱ࡿࠥ⋇").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack11lll1_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ⋈"), default=bstack11lll1_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢ⋉"), help=bstack11lll1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣ⋊"))
    parser.addoption(bstack11lll1_opy_ (u"ࠥ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ⋋"), default=bstack11lll1_opy_ (u"ࠦࡋࡧ࡬ࡴࡧࠥ⋌"), help=bstack11lll1_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯ࡣࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠦ⋍"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11lll1_opy_ (u"ࠨ࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠣ⋎"), action=bstack11lll1_opy_ (u"ࠢࡴࡶࡲࡶࡪࠨ⋏"), default=bstack11lll1_opy_ (u"ࠣࡥ࡫ࡶࡴࡳࡥࠣ⋐"),
                         help=bstack11lll1_opy_ (u"ࠤࡇࡶ࡮ࡼࡥࡳࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳࠣ⋑"))
def bstack1l11lll1_opy_(log):
    if not (log[bstack11lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⋒")] and log[bstack11lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⋓")].strip()):
        return
    active = bstack1llll1l1_opy_()
    log = {
        bstack11lll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⋔"): log[bstack11lll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⋕")],
        bstack11lll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⋖"): bstack11lll1l1_opy_().isoformat() + bstack11lll1_opy_ (u"ࠨ࡜ࠪ⋗"),
        bstack11lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⋘"): log[bstack11lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⋙")],
    }
    if active:
        if active[bstack11lll1_opy_ (u"ࠫࡹࡿࡰࡦࠩ⋚")] == bstack11lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⋛"):
            log[bstack11lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⋜")] = active[bstack11lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⋝")]
        elif active[bstack11lll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭⋞")] == bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺࠧ⋟"):
            log[bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⋠")] = active[bstack11lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⋡")]
    bstack1ll1l11l_opy_.bstack1ll1l111_opy_([log])
def bstack1llll1l1_opy_():
    if len(store[bstack11lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⋢")]) > 0 and store[bstack11lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⋣")][-1]:
        return {
            bstack11lll1_opy_ (u"ࠧࡵࡻࡳࡩࠬ⋤"): bstack11lll1_opy_ (u"ࠨࡪࡲࡳࡰ࠭⋥"),
            bstack11lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⋦"): store[bstack11lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ⋧")][-1]
        }
    if store.get(bstack11lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ⋨"), None):
        return {
            bstack11lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪ⋩"): bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷࠫ⋪"),
            bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⋫"): store[bstack11lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⋬")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.INIT_TEST, bstack1llll11l111_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.INIT_TEST, bstack1llll11l111_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.TEST, bstack1llll11l111_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1lll1lllll1l_opy_ = True
        bstack11ll111l11_opy_ = bstack111ll11l_opy_.bstack11111l1ll_opy_(bstack1111ll1ll1l_opy_(item.own_markers))
        if not cli.bstack1l1l1llll1l_opy_(bstack1l1l111l111_opy_):
            item._a11y_test_case = bstack11ll111l11_opy_
            if bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ⋭"), None):
                driver = getattr(item, bstack11lll1_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫ⋮"), None)
                item._a11y_started = bstack111ll11l_opy_.bstack1l11ll1l1_opy_(driver, bstack11ll111l11_opy_)
        if not bstack1ll1l11l_opy_.on() or bstack1lll1ll1ll11_opy_ != bstack11lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ⋯"):
            return
        global current_test_uuid #, bstack11llll11_opy_
        bstack1l111ll1_opy_ = {
            bstack11lll1_opy_ (u"ࠬࡻࡵࡪࡦࠪ⋰"): uuid4().__str__(),
            bstack11lll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⋱"): bstack11lll1l1_opy_().isoformat() + bstack11lll1_opy_ (u"࡛ࠧࠩ⋲")
        }
        current_test_uuid = bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⋳")]
        store[bstack11lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⋴")] = bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⋵")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l11l11l_opy_[item.nodeid] = {**_1l11l11l_opy_[item.nodeid], **bstack1l111ll1_opy_}
        bstack1lll1ll11l1l_opy_(item, _1l11l11l_opy_[item.nodeid], bstack11lll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⋶"))
    except Exception as err:
        print(bstack11lll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡩࡡ࡭࡮࠽ࠤࢀࢃࠧ⋷"), str(err))
def pytest_runtest_setup(item):
    store[bstack11lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⋸")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.BEFORE_EACH, bstack1llll11l111_opy_.PRE, item, bstack11lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⋹"))
    if bstack11111lll_opy_.bstack11l11111l1l_opy_():
            bstack1lll1lllll11_opy_ = bstack11lll1_opy_ (u"ࠣࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡣࡶࠤࡹ࡮ࡥࠡࡣࡥࡳࡷࡺࠠࡣࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡪࡾࡩࡴࡶࡶ࠲ࠧ⋺")
            logger.error(bstack1lll1lllll11_opy_)
            bstack1l111ll1_opy_ = {
                bstack11lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⋻"): uuid4().__str__(),
                bstack11lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⋼"): bstack11lll1l1_opy_().isoformat() + bstack11lll1_opy_ (u"ࠫ࡟࠭⋽"),
                bstack11lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⋾"): bstack11lll1l1_opy_().isoformat() + bstack11lll1_opy_ (u"࡚࠭ࠨ⋿"),
                bstack11lll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⌀"): bstack11lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ⌁"),
                bstack11lll1_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ⌂"): bstack1lll1lllll11_opy_,
                bstack11lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⌃"): [],
                bstack11lll1_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭⌄"): []
            }
            bstack1lll1ll11l1l_opy_(item, bstack1l111ll1_opy_, bstack11lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭⌅"))
            pytest.skip(bstack1lll1lllll11_opy_)
            return # skip all existing operations
    global bstack1lll1llllll1_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111l11l1l11_opy_():
        atexit.register(bstack11l11lll1_opy_)
        if not bstack1lll1llllll1_opy_:
            try:
                bstack1lll1llll1ll_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack1111l11llll_opy_():
                    bstack1lll1llll1ll_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1llll1ll_opy_:
                    signal.signal(s, bstack1llll1111111_opy_)
                bstack1lll1llllll1_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨ࡫࡮ࡹࡴࡦࡴࠣࡷ࡮࡭࡮ࡢ࡮ࠣ࡬ࡦࡴࡤ࡭ࡧࡵࡷ࠿ࠦࠢ⌆") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l111l1l1l_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⌇")
    try:
        if not bstack1ll1l11l_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack1l111ll1_opy_ = {
            bstack11lll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⌈"): uuid,
            bstack11lll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⌉"): bstack11lll1l1_opy_().isoformat() + bstack11lll1_opy_ (u"ࠪ࡞ࠬ⌊"),
            bstack11lll1_opy_ (u"ࠫࡹࡿࡰࡦࠩ⌋"): bstack11lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⌌"),
            bstack11lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩ⌍"): bstack11lll1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬ⌎"),
            bstack11lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫ⌏"): bstack11lll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ⌐")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ⌑")] = item
        store[bstack11lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⌒")] = [uuid]
        if not _1l11l11l_opy_.get(item.nodeid, None):
            _1l11l11l_opy_[item.nodeid] = {bstack11lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⌓"): [], bstack11lll1_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ⌔"): []}
        _1l11l11l_opy_[item.nodeid][bstack11lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⌕")].append(bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⌖")])
        _1l11l11l_opy_[item.nodeid + bstack11lll1_opy_ (u"ࠩ࠰ࡷࡪࡺࡵࡱࠩ⌗")] = bstack1l111ll1_opy_
        bstack1lll1ll1l11l_opy_(item, bstack1l111ll1_opy_, bstack11lll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ⌘"))
    except Exception as err:
        print(bstack11lll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡸ࡫ࡴࡶࡲ࠽ࠤࢀࢃࠧ⌙"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.TEST, bstack1llll11l111_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.AFTER_EACH, bstack1llll11l111_opy_.PRE, item, bstack11lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ⌚"))
        return # skip all existing operations
    try:
        global bstack1l111l1l11_opy_
        bstack1lll11ll11_opy_ = 0
        if bstack1l1111111_opy_ is True:
            bstack1lll11ll11_opy_ = int(os.environ.get(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭⌛")))
        if bstack11l1lll11_opy_.bstack1l1l1lllll_opy_() == bstack11lll1_opy_ (u"ࠢࡵࡴࡸࡩࠧ⌜"):
            if bstack11l1lll11_opy_.bstack11l1l11l1_opy_() == bstack11lll1_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥ⌝"):
                bstack1lll1lll1lll_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⌞"), None)
                bstack1l111l11l_opy_ = bstack1lll1lll1lll_opy_ + bstack11lll1_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨ⌟")
                driver = getattr(item, bstack11lll1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ⌠"), None)
                bstack1l1ll1llll_opy_ = getattr(item, bstack11lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ⌡"), None)
                bstack1lllllllll_opy_ = getattr(item, bstack11lll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⌢"), None)
                PercySDK.screenshot(driver, bstack1l111l11l_opy_, bstack1l1ll1llll_opy_=bstack1l1ll1llll_opy_, bstack1lllllllll_opy_=bstack1lllllllll_opy_, bstack1l1ll11lll_opy_=bstack1lll11ll11_opy_)
        if not cli.bstack1l1l1llll1l_opy_(bstack1l1l111l111_opy_):
            if getattr(item, bstack11lll1_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡳࡵࡣࡵࡸࡪࡪࠧ⌣"), False):
                bstack1lllllll1_opy_.bstack1lllll1ll_opy_(getattr(item, bstack11lll1_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ⌤"), None), bstack1l111l1l11_opy_, logger, item)
        if not bstack1ll1l11l_opy_.on():
            return
        bstack1l111ll1_opy_ = {
            bstack11lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⌥"): uuid4().__str__(),
            bstack11lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⌦"): bstack11lll1l1_opy_().isoformat() + bstack11lll1_opy_ (u"ࠫ࡟࠭⌧"),
            bstack11lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪ⌨"): bstack11lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ〈"),
            bstack11lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ〉"): bstack11lll1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬ⌫"),
            bstack11lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬ⌬"): bstack11lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬ⌭")
        }
        _1l11l11l_opy_[item.nodeid + bstack11lll1_opy_ (u"ࠫ࠲ࡺࡥࡢࡴࡧࡳࡼࡴࠧ⌮")] = bstack1l111ll1_opy_
        bstack1lll1ll1l11l_opy_(item, bstack1l111ll1_opy_, bstack11lll1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⌯"))
    except Exception as err:
        print(bstack11lll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮࠻ࠢࡾࢁࠬ⌰"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l111l1111_opy_(fixturedef.argname):
        store[bstack11lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭⌱")] = request.node
    elif bstack11l111ll1l1_opy_(fixturedef.argname):
        store[bstack11lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡦࡰࡦࡹࡳࡠ࡫ࡷࡩࡲ࠭⌲")] = request.node
    if not bstack1ll1l11l_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.SETUP_FIXTURE, bstack1llll11l111_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.SETUP_FIXTURE, bstack1llll11l111_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.SETUP_FIXTURE, bstack1llll11l111_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.SETUP_FIXTURE, bstack1llll11l111_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    try:
        fixture = {
            bstack11lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ⌳"): fixturedef.argname,
            bstack11lll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⌴"): bstack1111lll11ll_opy_(outcome),
            bstack11lll1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭⌵"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ⌶")]
        if not _1l11l11l_opy_.get(current_test_item.nodeid, None):
            _1l11l11l_opy_[current_test_item.nodeid] = {bstack11lll1_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ⌷"): []}
        _1l11l11l_opy_[current_test_item.nodeid][bstack11lll1_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⌸")].append(fixture)
    except Exception as err:
        logger.debug(bstack11lll1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫ⌹"), str(err))
if bstack1lll1ll11l_opy_() and bstack1ll1l11l_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.STEP, bstack1llll11l111_opy_.PRE, request, step)
            return
        try:
            _1l11l11l_opy_[request.node.nodeid][bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ⌺")].bstack11l1ll11_opy_(id(step))
        except Exception as err:
            print(bstack11lll1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳ࠾ࠥࢁࡽࠨ⌻"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.STEP, bstack1llll11l111_opy_.POST, request, step, exception)
            return
        try:
            _1l11l11l_opy_[request.node.nodeid][bstack11lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⌼")].bstack1ll1l1l1_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11lll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩ⌽"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.STEP, bstack1llll11l111_opy_.POST, request, step)
            return
        try:
            bstack1l11l111_opy_: bstack1ll11lll_opy_ = _1l11l11l_opy_[request.node.nodeid][bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ⌾")]
            bstack1l11l111_opy_.bstack1ll1l1l1_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11lll1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡷࡹ࡫ࡰࡠࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫ⌿"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1ll1ll11_opy_
        try:
            if not bstack1ll1l11l_opy_.on() or bstack1lll1ll1ll11_opy_ != bstack11lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬ⍀"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.TEST, bstack1llll11l111_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ⍁"), None)
            if not _1l11l11l_opy_.get(request.node.nodeid, None):
                _1l11l11l_opy_[request.node.nodeid] = {}
            bstack1l11l111_opy_ = bstack1ll11lll_opy_.bstack111111l1ll1_opy_(
                scenario, feature, request.node,
                name=bstack11l111l1ll1_opy_(request.node, scenario),
                started_at=bstack1l1111l1_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11lll1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬ⍂"),
                tags=bstack11l111ll11l_opy_(feature, scenario),
                bstack1l1l11l1_opy_=bstack1ll1l11l_opy_.bstack1l111111_opy_(driver) if driver and driver.session_id else {}
            )
            _1l11l11l_opy_[request.node.nodeid][bstack11lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⍃")] = bstack1l11l111_opy_
            bstack1lll1ll1l111_opy_(bstack1l11l111_opy_.uuid)
            bstack1ll1l11l_opy_.bstack11lll11l_opy_(bstack11lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⍄"), bstack1l11l111_opy_)
        except Exception as err:
            print(bstack11lll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨ⍅"), str(err))
def bstack1lll1lll1111_opy_(bstack11l1l11l_opy_):
    if bstack11l1l11l_opy_ in store[bstack11lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⍆")]:
        store[bstack11lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⍇")].remove(bstack11l1l11l_opy_)
def bstack1lll1ll1l111_opy_(test_uuid):
    store[bstack11lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⍈")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1ll1l11l_opy_.bstack1llll11l1l1l_opy_
def bstack1lll1llll11l_opy_(item, call, report):
    logger.debug(bstack11lll1_opy_ (u"ࠪ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡳࡵࡣࡵࡸࠬ⍉"))
    global bstack1lll1ll1ll11_opy_
    bstack11lll1ll1l_opy_ = bstack1l1111l1_opy_()
    if hasattr(report, bstack11lll1_opy_ (u"ࠫࡸࡺ࡯ࡱࠩ⍊")):
        bstack11lll1ll1l_opy_ = bstack1111l1ll1l1_opy_(report.stop)
    elif hasattr(report, bstack11lll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࠫ⍋")):
        bstack11lll1ll1l_opy_ = bstack1111l1ll1l1_opy_(report.start)
    try:
        if getattr(report, bstack11lll1_opy_ (u"࠭ࡷࡩࡧࡱࠫ⍌"), bstack11lll1_opy_ (u"ࠧࠨ⍍")) == bstack11lll1_opy_ (u"ࠨࡥࡤࡰࡱ࠭⍎"):
            logger.debug(bstack11lll1_opy_ (u"ࠩ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡹࡴࡢࡶࡨࠤ࠲ࠦࡻࡾ࠮ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦ࠭ࠡࡽࢀࠫ⍏").format(getattr(report, bstack11lll1_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⍐"), bstack11lll1_opy_ (u"ࠫࠬ⍑")).__str__(), bstack1lll1ll1ll11_opy_))
            if bstack1lll1ll1ll11_opy_ == bstack11lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ⍒"):
                _1l11l11l_opy_[item.nodeid][bstack11lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⍓")] = bstack11lll1ll1l_opy_
                bstack1lll1ll11l1l_opy_(item, _1l11l11l_opy_[item.nodeid], bstack11lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⍔"), report, call)
                store[bstack11lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⍕")] = None
            elif bstack1lll1ll1ll11_opy_ == bstack11lll1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨ⍖"):
                bstack1l11l111_opy_ = _1l11l11l_opy_[item.nodeid][bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⍗")]
                bstack1l11l111_opy_.set(hooks=_1l11l11l_opy_[item.nodeid].get(bstack11lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⍘"), []))
                exception, bstack11llll1l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11llll1l_opy_ = [call.excinfo.exconly(), getattr(report, bstack11lll1_opy_ (u"ࠬࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠫ⍙"), bstack11lll1_opy_ (u"࠭ࠧ⍚"))]
                bstack1l11l111_opy_.stop(time=bstack11lll1ll1l_opy_, result=Result(result=getattr(report, bstack11lll1_opy_ (u"ࠧࡰࡷࡷࡧࡴࡳࡥࠨ⍛"), bstack11lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⍜")), exception=exception, bstack11llll1l_opy_=bstack11llll1l_opy_))
                bstack1ll1l11l_opy_.bstack11lll11l_opy_(bstack11lll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⍝"), _1l11l11l_opy_[item.nodeid][bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⍞")])
        elif getattr(report, bstack11lll1_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⍟"), bstack11lll1_opy_ (u"ࠬ࠭⍠")) in [bstack11lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ⍡"), bstack11lll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ⍢")]:
            logger.debug(bstack11lll1_opy_ (u"ࠨࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡸࡺࡡࡵࡧࠣ࠱ࠥࢁࡽ࠭ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࠳ࠠࡼࡿࠪ⍣").format(getattr(report, bstack11lll1_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ⍤"), bstack11lll1_opy_ (u"ࠪࠫ⍥")).__str__(), bstack1lll1ll1ll11_opy_))
            bstack1l1lll11_opy_ = item.nodeid + bstack11lll1_opy_ (u"ࠫ࠲࠭⍦") + getattr(report, bstack11lll1_opy_ (u"ࠬࡽࡨࡦࡰࠪ⍧"), bstack11lll1_opy_ (u"࠭ࠧ⍨"))
            if getattr(report, bstack11lll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⍩"), False):
                hook_type = bstack11lll1_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭⍪") if getattr(report, bstack11lll1_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ⍫"), bstack11lll1_opy_ (u"ࠪࠫ⍬")) == bstack11lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ⍭") else bstack11lll1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩ⍮")
                _1l11l11l_opy_[bstack1l1lll11_opy_] = {
                    bstack11lll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⍯"): uuid4().__str__(),
                    bstack11lll1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⍰"): bstack11lll1ll1l_opy_,
                    bstack11lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ⍱"): hook_type
                }
            _1l11l11l_opy_[bstack1l1lll11_opy_][bstack11lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⍲")] = bstack11lll1ll1l_opy_
            bstack1lll1lll1111_opy_(_1l11l11l_opy_[bstack1l1lll11_opy_][bstack11lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⍳")])
            bstack1lll1ll1l11l_opy_(item, _1l11l11l_opy_[bstack1l1lll11_opy_], bstack11lll1_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭⍴"), report, call)
            if getattr(report, bstack11lll1_opy_ (u"ࠬࡽࡨࡦࡰࠪ⍵"), bstack11lll1_opy_ (u"࠭ࠧ⍶")) == bstack11lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⍷"):
                if getattr(report, bstack11lll1_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩ⍸"), bstack11lll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⍹")) == bstack11lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⍺"):
                    bstack1l111ll1_opy_ = {
                        bstack11lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩ⍻"): uuid4().__str__(),
                        bstack11lll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⍼"): bstack1l1111l1_opy_(),
                        bstack11lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⍽"): bstack1l1111l1_opy_()
                    }
                    _1l11l11l_opy_[item.nodeid] = {**_1l11l11l_opy_[item.nodeid], **bstack1l111ll1_opy_}
                    bstack1lll1ll11l1l_opy_(item, _1l11l11l_opy_[item.nodeid], bstack11lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ⍾"))
                    bstack1lll1ll11l1l_opy_(item, _1l11l11l_opy_[item.nodeid], bstack11lll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⍿"), report, call)
    except Exception as err:
        print(bstack11lll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࢀࢃࠧ⎀"), str(err))
def bstack1lll1lll111l_opy_(test, bstack1l111ll1_opy_, result=None, call=None, bstack1l11lll11l_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l11l111_opy_ = {
        bstack11lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⎁"): bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩ⎂")],
        bstack11lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪ⎃"): bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷࠫ⎄"),
        bstack11lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⎅"): test.name,
        bstack11lll1_opy_ (u"ࠨࡤࡲࡨࡾ࠭⎆"): {
            bstack11lll1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧ⎇"): bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ⎈"),
            bstack11lll1_opy_ (u"ࠫࡨࡵࡤࡦࠩ⎉"): inspect.getsource(test.obj)
        },
        bstack11lll1_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ⎊"): test.name,
        bstack11lll1_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬ⎋"): test.name,
        bstack11lll1_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧ⎌"): bstack1ll11l11_opy_.bstack1l1ll11l_opy_(test),
        bstack11lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ⎍"): file_path,
        bstack11lll1_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫ⎎"): file_path,
        bstack11lll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⎏"): bstack11lll1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ⎐"),
        bstack11lll1_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪ⎑"): file_path,
        bstack11lll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⎒"): bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⎓")],
        bstack11lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ⎔"): bstack11lll1_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩ⎕"),
        bstack11lll1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭⎖"): {
            bstack11lll1_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨ⎗"): test.nodeid
        },
        bstack11lll1_opy_ (u"ࠬࡺࡡࡨࡵࠪ⎘"): bstack1111ll1ll1l_opy_(test.own_markers)
    }
    if bstack1l11lll11l_opy_ in [bstack11lll1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧ⎙"), bstack11lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⎚")]:
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠨ࡯ࡨࡸࡦ࠭⎛")] = {
            bstack11lll1_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫ⎜"): bstack1l111ll1_opy_.get(bstack11lll1_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ⎝"), [])
        }
    if bstack1l11lll11l_opy_ == bstack11lll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬ⎞"):
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⎟")] = bstack11lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ⎠")
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⎡")] = bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⎢")]
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⎣")] = bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⎤")]
    if result:
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⎥")] = result.outcome
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭⎦")] = result.duration * 1000
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⎧")] = bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎨")]
        if result.failed:
            bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⎩")] = bstack1ll1l11l_opy_.bstack1111111l1l_opy_(call.excinfo.typename)
            bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ⎪")] = bstack1ll1l11l_opy_.bstack1llll1l111ll_opy_(call.excinfo, result)
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⎫")] = bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⎬")]
    if outcome:
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⎭")] = bstack1111lll11ll_opy_(outcome)
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ⎮")] = 0
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎯")] = bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⎰")]
        if bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⎱")] == bstack11lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⎲"):
            bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪ⎳")] = bstack11lll1_opy_ (u"࡛ࠬ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷ࠭⎴")  # bstack1lll1ll1l1ll_opy_
            bstack1l11l111_opy_[bstack11lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ⎵")] = [{bstack11lll1_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪ⎶"): [bstack11lll1_opy_ (u"ࠨࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠬ⎷")]}]
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⎸")] = bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⎹")]
    return bstack1l11l111_opy_
def bstack1llll111111l_opy_(test, bstack1ll11ll1_opy_, bstack1l11lll11l_opy_, result, call, outcome, bstack1lll1ll1l1l1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ⎺")]
    hook_name = bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨ⎻")]
    hook_data = {
        bstack11lll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⎼"): bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⎽")],
        bstack11lll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭⎾"): bstack11lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⎿"),
        bstack11lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨ⏀"): bstack11lll1_opy_ (u"ࠫࢀࢃࠧ⏁").format(bstack11l111lll11_opy_(hook_name)),
        bstack11lll1_opy_ (u"ࠬࡨ࡯ࡥࡻࠪ⏂"): {
            bstack11lll1_opy_ (u"࠭࡬ࡢࡰࡪࠫ⏃"): bstack11lll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ⏄"),
            bstack11lll1_opy_ (u"ࠨࡥࡲࡨࡪ࠭⏅"): None
        },
        bstack11lll1_opy_ (u"ࠩࡶࡧࡴࡶࡥࠨ⏆"): test.name,
        bstack11lll1_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪ⏇"): bstack1ll11l11_opy_.bstack1l1ll11l_opy_(test, hook_name),
        bstack11lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ⏈"): file_path,
        bstack11lll1_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧ⏉"): file_path,
        bstack11lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⏊"): bstack11lll1_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ⏋"),
        bstack11lll1_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭⏌"): file_path,
        bstack11lll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⏍"): bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⏎")],
        bstack11lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ⏏"): bstack11lll1_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧ⏐") if bstack1lll1ll1ll11_opy_ == bstack11lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪ⏑") else bstack11lll1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧ⏒"),
        bstack11lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ⏓"): hook_type
    }
    bstack1l11111ll1l_opy_ = bstack1llll111_opy_(_1l11l11l_opy_.get(test.nodeid, None))
    if bstack1l11111ll1l_opy_:
        hook_data[bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡮ࡪࠧ⏔")] = bstack1l11111ll1l_opy_
    if result:
        hook_data[bstack11lll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⏕")] = result.outcome
        hook_data[bstack11lll1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⏖")] = result.duration * 1000
        hook_data[bstack11lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏗")] = bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⏘")]
        if result.failed:
            hook_data[bstack11lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭⏙")] = bstack1ll1l11l_opy_.bstack1111111l1l_opy_(call.excinfo.typename)
            hook_data[bstack11lll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ⏚")] = bstack1ll1l11l_opy_.bstack1llll1l111ll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11lll1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⏛")] = bstack1111lll11ll_opy_(outcome)
        hook_data[bstack11lll1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ⏜")] = 100
        hook_data[bstack11lll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏝")] = bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏞")]
        if hook_data[bstack11lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⏟")] == bstack11lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⏠"):
            hook_data[bstack11lll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⏡")] = bstack11lll1_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪ⏢")  # bstack1lll1ll1l1ll_opy_
            hook_data[bstack11lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ⏣")] = [{bstack11lll1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ⏤"): [bstack11lll1_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩ⏥")]}]
    if bstack1lll1ll1l1l1_opy_:
        hook_data[bstack11lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⏦")] = bstack1lll1ll1l1l1_opy_.result
        hook_data[bstack11lll1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ⏧")] = bstack111l111111l_opy_(bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⏨")], bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⏩")])
        hook_data[bstack11lll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⏪")] = bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏫")]
        if hook_data[bstack11lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⏬")] == bstack11lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭⏭"):
            hook_data[bstack11lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭⏮")] = bstack1ll1l11l_opy_.bstack1111111l1l_opy_(bstack1lll1ll1l1l1_opy_.exception_type)
            hook_data[bstack11lll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ⏯")] = [{bstack11lll1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ⏰"): bstack111l11lllll_opy_(bstack1lll1ll1l1l1_opy_.exception)}]
    return hook_data
def bstack1lll1ll11l1l_opy_(test, bstack1l111ll1_opy_, bstack1l11lll11l_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack11lll1_opy_ (u"ࠪࡷࡪࡴࡤࡠࡶࡨࡷࡹࡥࡲࡶࡰࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡺࡥࡴࡶࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠢ࠰ࠤࢀࢃࠧ⏱").format(bstack1l11lll11l_opy_))
    bstack1l11l111_opy_ = bstack1lll1lll111l_opy_(test, bstack1l111ll1_opy_, result, call, bstack1l11lll11l_opy_, outcome)
    driver = getattr(test, bstack11lll1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ⏲"), None)
    if bstack1l11lll11l_opy_ == bstack11lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⏳") and driver:
        bstack1l11l111_opy_[bstack11lll1_opy_ (u"࠭ࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠬ⏴")] = bstack1ll1l11l_opy_.bstack1l111111_opy_(driver)
    if bstack1l11lll11l_opy_ == bstack11lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ⏵"):
        bstack1l11lll11l_opy_ = bstack11lll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⏶")
    bstack1lll1l11_opy_ = {
        bstack11lll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⏷"): bstack1l11lll11l_opy_,
        bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ⏸"): bstack1l11l111_opy_
    }
    bstack1ll1l11l_opy_.bstack1lllll11_opy_(bstack1lll1l11_opy_)
    if bstack1l11lll11l_opy_ == bstack11lll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⏹"):
        threading.current_thread().bstackTestMeta = {bstack11lll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⏺"): bstack11lll1_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ⏻")}
    elif bstack1l11lll11l_opy_ == bstack11lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⏼"):
        threading.current_thread().bstackTestMeta = {bstack11lll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⏽"): getattr(result, bstack11lll1_opy_ (u"ࠩࡲࡹࡹࡩ࡯࡮ࡧࠪ⏾"), bstack11lll1_opy_ (u"ࠪࠫ⏿"))}
def bstack1lll1ll1l11l_opy_(test, bstack1l111ll1_opy_, bstack1l11lll11l_opy_, result=None, call=None, outcome=None, bstack1lll1ll1l1l1_opy_=None):
    logger.debug(bstack11lll1_opy_ (u"ࠫࡸ࡫࡮ࡥࡡ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡨࡰࡱ࡮ࠤࡩࡧࡴࡢ࠮ࠣࡩࡻ࡫࡮ࡵࡖࡼࡴࡪࠦ࠭ࠡࡽࢀࠫ␀").format(bstack1l11lll11l_opy_))
    hook_data = bstack1llll111111l_opy_(test, bstack1l111ll1_opy_, bstack1l11lll11l_opy_, result, call, outcome, bstack1lll1ll1l1l1_opy_)
    bstack1lll1l11_opy_ = {
        bstack11lll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ␁"): bstack1l11lll11l_opy_,
        bstack11lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨ␂"): hook_data
    }
    bstack1ll1l11l_opy_.bstack1lllll11_opy_(bstack1lll1l11_opy_)
def bstack1llll111_opy_(bstack1l111ll1_opy_):
    if not bstack1l111ll1_opy_:
        return None
    if bstack1l111ll1_opy_.get(bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ␃"), None):
        return getattr(bstack1l111ll1_opy_[bstack11lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ␄")], bstack11lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ␅"), None)
    return bstack1l111ll1_opy_.get(bstack11lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ␆"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.LOG, bstack1llll11l111_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.LOG, bstack1llll11l111_opy_.POST, request, caplog)
        return # skip all existing operations
    try:
        if not bstack1ll1l11l_opy_.on():
            return
        places = [bstack11lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ␇"), bstack11lll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ␈"), bstack11lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ␉")]
        logs = []
        for bstack1lll1ll1llll_opy_ in places:
            records = caplog.get_records(bstack1lll1ll1llll_opy_)
            bstack1lll1lll1l1l_opy_ = bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ␊") if bstack1lll1ll1llll_opy_ == bstack11lll1_opy_ (u"ࠨࡥࡤࡰࡱ࠭␋") else bstack11lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ␌")
            bstack1lll1llll1l1_opy_ = request.node.nodeid + (bstack11lll1_opy_ (u"ࠪࠫ␍") if bstack1lll1ll1llll_opy_ == bstack11lll1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ␎") else bstack11lll1_opy_ (u"ࠬ࠳ࠧ␏") + bstack1lll1ll1llll_opy_)
            test_uuid = bstack1llll111_opy_(_1l11l11l_opy_.get(bstack1lll1llll1l1_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack111l11l111l_opy_(record.message):
                    continue
                logs.append({
                    bstack11lll1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ␐"): bstack111l1ll1ll1_opy_(record.created).isoformat() + bstack11lll1_opy_ (u"࡛ࠧࠩ␑"),
                    bstack11lll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ␒"): record.levelname,
                    bstack11lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ␓"): record.message,
                    bstack1lll1lll1l1l_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1ll1l11l_opy_.bstack1ll1l111_opy_(logs)
    except Exception as err:
        print(bstack11lll1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡨࡵ࡮ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧ࠽ࠤࢀࢃࠧ␔"), str(err))
def bstack11l1lll1l1_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1111l11111_opy_
    bstack11ll11l11_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ␕"), None) and bstack1lll111l_opy_(
            threading.current_thread(), bstack11lll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ␖"), None)
    bstack1l1ll1l1l_opy_ = getattr(driver, bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭␗"), None) != None and getattr(driver, bstack11lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ␘"), None) == True
    if sequence == bstack11lll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ␙") and driver != None:
      if not bstack1111l11111_opy_ and bstack1lll1l11111_opy_() and bstack11lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ␚") in CONFIG and CONFIG[bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ␛")] == True and bstack11ll1111l_opy_.bstack1l11l11l1_opy_(driver_command) and (bstack1l1ll1l1l_opy_ or bstack11ll11l11_opy_) and not bstack1ll1ll111l_opy_(args):
        try:
          bstack1111l11111_opy_ = True
          logger.debug(bstack11lll1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡿࢂ࠭␜").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11lll1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡶࡧࡦࡴࠠࡼࡿࠪ␝").format(str(err)))
        bstack1111l11111_opy_ = False
    if sequence == bstack11lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ␞"):
        if driver_command == bstack11lll1_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫ␟"):
            bstack1ll1l11l_opy_.bstack111ll11lll_opy_({
                bstack11lll1_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ␠"): response[bstack11lll1_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ␡")],
                bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ␢"): store[bstack11lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ␣")]
            })
def bstack11l11lll1_opy_():
    global bstack1l1l11l11l_opy_
    bstack1l1l1llll1_opy_.bstack11llll11l_opy_()
    logging.shutdown()
    bstack1ll1l11l_opy_.bstack1ll1111l_opy_()
    for driver in bstack1l1l11l11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1llll1111111_opy_(*args):
    global bstack1l1l11l11l_opy_
    bstack1ll1l11l_opy_.bstack1ll1111l_opy_()
    for driver in bstack1l1l11l11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11lll11l1_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack11lll111ll_opy_(self, *args, **kwargs):
    bstack1lll111lll_opy_ = bstack1111lll1ll_opy_(self, *args, **kwargs)
    bstack1l1111l11l_opy_ = getattr(threading.current_thread(), bstack11lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭␤"), None)
    if bstack1l1111l11l_opy_ and bstack1l1111l11l_opy_.get(bstack11lll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭␥"), bstack11lll1_opy_ (u"ࠧࠨ␦")) == bstack11lll1_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ␧"):
        bstack1ll1l11l_opy_.bstack111llll11l_opy_(self)
    return bstack1lll111lll_opy_
@measure(event_name=EVENTS.bstack1ll11111l1_opy_, stage=STAGE.bstack1ll1ll11l_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack11l11111l1_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1lll1l11l_opy_ = Config.bstack111ll1l1_opy_()
    if bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭␨")):
        return
    bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧ␩"), True)
    global bstack11lll1l11l_opy_
    global bstack111l1ll11l_opy_
    bstack11lll1l11l_opy_ = framework_name
    logger.info(bstack1l11lllll_opy_.format(bstack11lll1l11l_opy_.split(bstack11lll1_opy_ (u"ࠫ࠲࠭␪"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1lll1l11111_opy_():
            Service.start = bstack11111l1l1l_opy_
            Service.stop = bstack11111llll1_opy_
            webdriver.Remote.get = bstack1l11l1l11l_opy_
            webdriver.Remote.__init__ = bstack111lllll11_opy_
            if not isinstance(os.getenv(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭␫")), str):
                return
            WebDriver.quit = bstack111lll11l_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1ll1l11l_opy_.on():
            webdriver.Remote.__init__ = bstack11lll111ll_opy_
        bstack111l1ll11l_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack11lll1_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫ␬")):
        bstack111l1ll11l_opy_ = eval(os.environ.get(bstack11lll1_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬ␭")))
    if not bstack111l1ll11l_opy_:
        bstack11l1l11l11_opy_(bstack11lll1_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥ␮"), bstack1l1lll11l_opy_)
    if bstack1l1ll11l1l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack11lll1_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ␯")) and callable(getattr(RemoteConnection, bstack11lll1_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ␰"))):
                RemoteConnection._get_proxy_url = bstack111ll11ll1_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack111ll11ll1_opy_
        except Exception as e:
            logger.error(bstack111l1l11ll_opy_.format(str(e)))
    if bstack11lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ␱") in str(framework_name).lower():
        if not bstack1lll1l11111_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1111lll1l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll11l1l11_opy_
            Config.getoption = bstack1l11l11ll_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1l1l1lll11_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack111lll1l11_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack111lll11l_opy_(self):
    global bstack11lll1l11l_opy_
    global bstack111l1l1l1l_opy_
    global bstack1l1ll11ll1_opy_
    try:
        if bstack11lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ␲") in bstack11lll1l11l_opy_ and self.session_id != None and bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪ␳"), bstack11lll1_opy_ (u"ࠧࠨ␴")) != bstack11lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ␵"):
            bstack11l1l1l1ll_opy_ = bstack11lll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ␶") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ␷")
            bstack1l11l11l1l_opy_(logger, True)
            if os.environ.get(bstack11lll1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧ␸"), None):
                self.execute_script(
                    bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪ␹") + json.dumps(
                        os.environ.get(bstack11lll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ␺"))) + bstack11lll1_opy_ (u"ࠧࡾࡿࠪ␻"))
            if self != None:
                bstack1lllll1l1l_opy_(self, bstack11l1l1l1ll_opy_, bstack11lll1_opy_ (u"ࠨ࠮ࠣࠫ␼").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1l1l1llll1l_opy_(bstack1l1l111l111_opy_):
            item = store.get(bstack11lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭␽"), None)
            if item is not None and bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ␾"), None):
                bstack1lllllll1_opy_.bstack1lllll1ll_opy_(self, bstack1l111l1l11_opy_, logger, item)
        threading.current_thread().testStatus = bstack11lll1_opy_ (u"ࠫࠬ␿")
    except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨ⑀") + str(e))
    bstack1l1ll11ll1_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1lll11111l_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack111lllll11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack111l1l1l1l_opy_
    global bstack1l11llll1_opy_
    global bstack1l1111111_opy_
    global bstack11lll1l11l_opy_
    global bstack1111lll1ll_opy_
    global bstack1l1l11l11l_opy_
    global bstack111111ll1l_opy_
    global bstack1l1111lll1_opy_
    global bstack1l111l1l11_opy_
    CONFIG[bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ⑁")] = str(bstack11lll1l11l_opy_) + str(__version__)
    command_executor = bstack11lll1lll1_opy_(bstack111111ll1l_opy_, CONFIG)
    logger.debug(bstack1l1l11111_opy_.format(command_executor))
    proxy = bstack1l11l1lll1_opy_(CONFIG, proxy)
    bstack1lll11ll11_opy_ = 0
    try:
        if bstack1l1111111_opy_ is True:
            bstack1lll11ll11_opy_ = int(os.environ.get(bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ⑂")))
    except:
        bstack1lll11ll11_opy_ = 0
    bstack11lll11l1l_opy_ = bstack11lllll111_opy_(CONFIG, bstack1lll11ll11_opy_)
    logger.debug(bstack11llll1ll1_opy_.format(str(bstack11lll11l1l_opy_)))
    bstack1l111l1l11_opy_ = CONFIG.get(bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ⑃"))[bstack1lll11ll11_opy_]
    if bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭⑄") in CONFIG and CONFIG[bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ⑅")]:
        bstack11l11111l_opy_(bstack11lll11l1l_opy_, bstack1l1111lll1_opy_)
    if bstack111ll11l_opy_.bstack1111l11lll_opy_(CONFIG, bstack1lll11ll11_opy_) and bstack111ll11l_opy_.bstack1l11l1111_opy_(bstack11lll11l1l_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1l1l1llll1l_opy_(bstack1l1l111l111_opy_):
            bstack111ll11l_opy_.set_capabilities(bstack11lll11l1l_opy_, CONFIG)
    if desired_capabilities:
        bstack11l111l11_opy_ = bstack11llll1111_opy_(desired_capabilities)
        bstack11l111l11_opy_[bstack11lll1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ⑆")] = bstack1111ll1ll1_opy_(CONFIG)
        bstack111llll111_opy_ = bstack11lllll111_opy_(bstack11l111l11_opy_)
        if bstack111llll111_opy_:
            bstack11lll11l1l_opy_ = update(bstack111llll111_opy_, bstack11lll11l1l_opy_)
        desired_capabilities = None
    if options:
        bstack11ll11lll_opy_(options, bstack11lll11l1l_opy_)
    if not options:
        options = bstack1ll111lll1_opy_(bstack11lll11l1l_opy_)
    if proxy and bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ⑇")):
        options.proxy(proxy)
    if options and bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ⑈")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack11lllll11l_opy_() < version.parse(bstack11lll1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭⑉")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack11lll11l1l_opy_)
    logger.info(bstack1llll1l1ll_opy_)
    bstack1111l111l1_opy_.end(EVENTS.bstack1ll11111l1_opy_.value, EVENTS.bstack1ll11111l1_opy_.value + bstack11lll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ⑊"),
                               EVENTS.bstack1ll11111l1_opy_.value + bstack11lll1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ⑋"), True, None)
    try:
        if bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ⑌")):
            bstack1111lll1ll_opy_(self, command_executor=command_executor,
                      options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
        elif bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ⑍")):
            bstack1111lll1ll_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities, options=options,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        elif bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬ⑎")):
            bstack1111lll1ll_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        else:
            bstack1111lll1ll_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive)
    except Exception as bstack1l1l11l1ll_opy_:
        logger.error(bstack11l111lll_opy_.format(bstack11lll1_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠬ⑏"), str(bstack1l1l11l1ll_opy_)))
        raise bstack1l1l11l1ll_opy_
    try:
        bstack1l1ll11ll_opy_ = bstack11lll1_opy_ (u"ࠧࠨ⑐")
        if bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࡢ࠲ࠩ⑑")):
            bstack1l1ll11ll_opy_ = self.caps.get(bstack11lll1_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ⑒"))
        else:
            bstack1l1ll11ll_opy_ = self.capabilities.get(bstack11lll1_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥ⑓"))
        if bstack1l1ll11ll_opy_:
            bstack1l1111ll1_opy_(bstack1l1ll11ll_opy_)
            if bstack11lllll11l_opy_() <= version.parse(bstack11lll1_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫ⑔")):
                self.command_executor._url = bstack11lll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ⑕") + bstack111111ll1l_opy_ + bstack11lll1_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥ⑖")
            else:
                self.command_executor._url = bstack11lll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤ⑗") + bstack1l1ll11ll_opy_ + bstack11lll1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤ⑘")
            logger.debug(bstack11ll1lll1_opy_.format(bstack1l1ll11ll_opy_))
        else:
            logger.debug(bstack111ll11111_opy_.format(bstack11lll1_opy_ (u"ࠤࡒࡴࡹ࡯࡭ࡢ࡮ࠣࡌࡺࡨࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥ⑙")))
    except Exception as e:
        logger.debug(bstack111ll11111_opy_.format(e))
    bstack111l1l1l1l_opy_ = self.session_id
    if bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ⑚") in bstack11lll1l11l_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ⑛"), None)
        if item:
            bstack1lll1lll11l1_opy_ = getattr(item, bstack11lll1_opy_ (u"ࠬࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࡡࡶࡸࡦࡸࡴࡦࡦࠪ⑜"), False)
            if not getattr(item, bstack11lll1_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧ⑝"), None) and bstack1lll1lll11l1_opy_:
                setattr(store[bstack11lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⑞")], bstack11lll1_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ⑟"), self)
        bstack1l1111l11l_opy_ = getattr(threading.current_thread(), bstack11lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪ①"), None)
        if bstack1l1111l11l_opy_ and bstack1l1111l11l_opy_.get(bstack11lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ②"), bstack11lll1_opy_ (u"ࠫࠬ③")) == bstack11lll1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭④"):
            bstack1ll1l11l_opy_.bstack111llll11l_opy_(self)
    bstack1l1l11l11l_opy_.append(self)
    if bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⑤") in CONFIG and bstack11lll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⑥") in CONFIG[bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ⑦")][bstack1lll11ll11_opy_]:
        bstack1l11llll1_opy_ = CONFIG[bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⑧")][bstack1lll11ll11_opy_][bstack11lll1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⑨")]
    logger.debug(bstack1l11l11lll_opy_.format(bstack111l1l1l1l_opy_))
@measure(event_name=EVENTS.bstack11l11lll11_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack1l11l1l11l_opy_(self, url):
    global bstack11l11ll1ll_opy_
    global CONFIG
    try:
        bstack111l1l1lll_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1111l1l1ll_opy_.format(str(err)))
    try:
        bstack11l11ll1ll_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack1l1ll1ll11_opy_):
                bstack111l1l1lll_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1111l1l1ll_opy_.format(str(err)))
        raise e
def bstack1l111ll1l1_opy_(item, when):
    global bstack11lll111l_opy_
    try:
        bstack11lll111l_opy_(item, when)
    except Exception as e:
        pass
def bstack1l1l1lll11_opy_(item, call, rep):
    global bstack1l111111l_opy_
    global bstack1l1l11l11l_opy_
    name = bstack11lll1_opy_ (u"ࠫࠬ⑩")
    try:
        if rep.when == bstack11lll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ⑪"):
            bstack111l1l1l1l_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack11lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⑫"))
            try:
                if (str(skipSessionName).lower() != bstack11lll1_opy_ (u"ࠧࡵࡴࡸࡩࠬ⑬")):
                    name = str(rep.nodeid)
                    bstack1llll111l1_opy_ = bstack11l111111l_opy_(bstack11lll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⑭"), name, bstack11lll1_opy_ (u"ࠩࠪ⑮"), bstack11lll1_opy_ (u"ࠪࠫ⑯"), bstack11lll1_opy_ (u"ࠫࠬ⑰"), bstack11lll1_opy_ (u"ࠬ࠭⑱"))
                    os.environ[bstack11lll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ⑲")] = name
                    for driver in bstack1l1l11l11l_opy_:
                        if bstack111l1l1l1l_opy_ == driver.session_id:
                            driver.execute_script(bstack1llll111l1_opy_)
            except Exception as e:
                logger.debug(bstack11lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ⑳").format(str(e)))
            try:
                bstack1111lll111_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ⑴"):
                    status = bstack11lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⑵") if rep.outcome.lower() == bstack11lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⑶") else bstack11lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ⑷")
                    reason = bstack11lll1_opy_ (u"ࠬ࠭⑸")
                    if status == bstack11lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭⑹"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11lll1_opy_ (u"ࠧࡪࡰࡩࡳࠬ⑺") if status == bstack11lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⑻") else bstack11lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ⑼")
                    data = name + bstack11lll1_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬ⑽") if status == bstack11lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ⑾") else name + bstack11lll1_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩࠧࠠࠨ⑿") + reason
                    bstack11ll1l1ll_opy_ = bstack11l111111l_opy_(bstack11lll1_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ⒀"), bstack11lll1_opy_ (u"ࠧࠨ⒁"), bstack11lll1_opy_ (u"ࠨࠩ⒂"), bstack11lll1_opy_ (u"ࠩࠪ⒃"), level, data)
                    for driver in bstack1l1l11l11l_opy_:
                        if bstack111l1l1l1l_opy_ == driver.session_id:
                            driver.execute_script(bstack11ll1l1ll_opy_)
            except Exception as e:
                logger.debug(bstack11lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤࡱࡱࡸࡪࡾࡴࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ⒄").format(str(e)))
    except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡤࡸࡪࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁࡽࠨ⒅").format(str(e)))
    bstack1l111111l_opy_(item, call, rep)
notset = Notset()
def bstack1l11l11ll_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11l111ll1_opy_
    if str(name).lower() == bstack11lll1_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬ⒆"):
        return bstack11lll1_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧ⒇")
    else:
        return bstack11l111ll1_opy_(self, name, default, skip)
def bstack111ll11ll1_opy_(self):
    global CONFIG
    global bstack1l11llllll_opy_
    try:
        proxy = bstack1l1l1l1ll_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11lll1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ⒈")):
                proxies = bstack1111llll1_opy_(proxy, bstack11lll1lll1_opy_())
                if len(proxies) > 0:
                    protocol, bstack11111ll11_opy_ = proxies.popitem()
                    if bstack11lll1_opy_ (u"ࠣ࠼࠲࠳ࠧ⒉") in bstack11111ll11_opy_:
                        return bstack11111ll11_opy_
                    else:
                        return bstack11lll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ⒊") + bstack11111ll11_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢ⒋").format(str(e)))
    return bstack1l11llllll_opy_(self)
def bstack1l1ll11l1l_opy_():
    return (bstack11lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ⒌") in CONFIG or bstack11lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ⒍") in CONFIG) and bstack1111l1l11l_opy_() and bstack11lllll11l_opy_() >= version.parse(
        bstack1ll1l1l111_opy_)
def bstack1llll1ll1l_opy_(self,
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
    global bstack1l11llll1_opy_
    global bstack1l1111111_opy_
    global bstack11lll1l11l_opy_
    CONFIG[bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ⒎")] = str(bstack11lll1l11l_opy_) + str(__version__)
    bstack1lll11ll11_opy_ = 0
    try:
        if bstack1l1111111_opy_ is True:
            bstack1lll11ll11_opy_ = int(os.environ.get(bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ⒏")))
    except:
        bstack1lll11ll11_opy_ = 0
    CONFIG[bstack11lll1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ⒐")] = True
    bstack11lll11l1l_opy_ = bstack11lllll111_opy_(CONFIG, bstack1lll11ll11_opy_)
    logger.debug(bstack11llll1ll1_opy_.format(str(bstack11lll11l1l_opy_)))
    if CONFIG.get(bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭⒑")):
        bstack11l11111l_opy_(bstack11lll11l1l_opy_, bstack1l1111lll1_opy_)
    if bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭⒒") in CONFIG and bstack11lll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⒓") in CONFIG[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⒔")][bstack1lll11ll11_opy_]:
        bstack1l11llll1_opy_ = CONFIG[bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⒕")][bstack1lll11ll11_opy_][bstack11lll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⒖")]
    import urllib
    import json
    if bstack11lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⒗") in CONFIG and str(CONFIG[bstack11lll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⒘")]).lower() != bstack11lll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ⒙"):
        bstack1l1l111l1l_opy_ = bstack1ll1ll1ll1_opy_()
        bstack111l11l111_opy_ = bstack1l1l111l1l_opy_ + urllib.parse.quote(json.dumps(bstack11lll11l1l_opy_))
    else:
        bstack111l11l111_opy_ = bstack11lll1_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭⒚") + urllib.parse.quote(json.dumps(bstack11lll11l1l_opy_))
    browser = self.connect(bstack111l11l111_opy_)
    return browser
def bstack11ll11llll_opy_():
    global bstack111l1ll11l_opy_
    global bstack11lll1l11l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111l11l11_opy_
        if not bstack1lll1l11111_opy_():
            global bstack111lll1l1l_opy_
            if not bstack111lll1l1l_opy_:
                from bstack_utils.helper import bstack11l1l1l11_opy_, bstack111l1lll11_opy_
                bstack111lll1l1l_opy_ = bstack11l1l1l11_opy_()
                bstack111l1lll11_opy_(bstack11lll1l11l_opy_)
            BrowserType.connect = bstack1111l11l11_opy_
            return
        BrowserType.launch = bstack1llll1ll1l_opy_
        bstack111l1ll11l_opy_ = True
    except Exception as e:
        pass
def bstack1lll1lll1ll1_opy_():
    global CONFIG
    global bstack1ll1l11111_opy_
    global bstack111111ll1l_opy_
    global bstack1l1111lll1_opy_
    global bstack1l1111111_opy_
    global bstack1l11ll1ll1_opy_
    CONFIG = json.loads(os.environ.get(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࠫ⒛")))
    bstack1ll1l11111_opy_ = eval(os.environ.get(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ⒜")))
    bstack111111ll1l_opy_ = os.environ.get(bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡈࡖࡄࡢ࡙ࡗࡒࠧ⒝"))
    bstack1ll11l1l1_opy_(CONFIG, bstack1ll1l11111_opy_)
    bstack1l11ll1ll1_opy_ = bstack1l1l1llll1_opy_.configure_logger(CONFIG, bstack1l11ll1ll1_opy_)
    if cli.bstack1ll11lllll_opy_():
        bstack1l1l1ll1l_opy_.invoke(Events.CONNECT, bstack11lll1ll1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ⒞"), bstack11lll1_opy_ (u"ࠩ࠳ࠫ⒟")))
        cli.bstack1l1l11111l1_opy_(cli_context.platform_index)
        cli.bstack1l1l11111ll_opy_(bstack11lll1lll1_opy_(bstack111111ll1l_opy_, CONFIG), cli_context.platform_index, bstack1ll111lll1_opy_)
        cli.bstack1l1l11l1ll1_opy_()
        logger.debug(bstack11lll1_opy_ (u"ࠥࡇࡑࡏࠠࡪࡵࠣࡥࡨࡺࡩࡷࡧࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤ⒠") + str(cli_context.platform_index) + bstack11lll1_opy_ (u"ࠦࠧ⒡"))
        return # skip all existing operations
    global bstack1111lll1ll_opy_
    global bstack1l1ll11ll1_opy_
    global bstack1l1l11l1l1_opy_
    global bstack1ll1ll1111_opy_
    global bstack111llll1l_opy_
    global bstack1l11l1l1ll_opy_
    global bstack1l11l1llll_opy_
    global bstack11l11ll1ll_opy_
    global bstack1l11llllll_opy_
    global bstack11l111ll1_opy_
    global bstack11lll111l_opy_
    global bstack1l111111l_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1111lll1ll_opy_ = webdriver.Remote.__init__
        bstack1l1ll11ll1_opy_ = WebDriver.quit
        bstack1l11l1llll_opy_ = WebDriver.close
        bstack11l11ll1ll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ⒢") in CONFIG or bstack11lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ⒣") in CONFIG) and bstack1111l1l11l_opy_():
        if bstack11lllll11l_opy_() < version.parse(bstack1ll1l1l111_opy_):
            logger.error(bstack1l1l1ll11_opy_.format(bstack11lllll11l_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack11lll1_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ⒤")) and callable(getattr(RemoteConnection, bstack11lll1_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ⒥"))):
                    bstack1l11llllll_opy_ = RemoteConnection._get_proxy_url
                else:
                    from selenium.webdriver.remote.client_config import ClientConfig
                    bstack1l11llllll_opy_ = ClientConfig.get_proxy_url
            except Exception as e:
                logger.error(bstack111l1l11ll_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack11l111ll1_opy_ = Config.getoption
        from _pytest import runner
        bstack11lll111l_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack111llll1_opy_)
    try:
        from pytest_bdd import reporting
        bstack1l111111l_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ⒦"))
    bstack1l1111lll1_opy_ = CONFIG.get(bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ⒧"), {}).get(bstack11lll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭⒨"))
    bstack1l1111111_opy_ = True
    bstack11l11111l1_opy_(bstack1ll11ll111_opy_)
if (bstack111l11l1l11_opy_()):
    bstack1lll1lll1ll1_opy_()
@error_handler(class_method=False)
def bstack1lll1ll1ll1l_opy_(hook_name, event, bstack1ll111ll11l_opy_=None):
    if hook_name not in [bstack11lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭⒩"), bstack11lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪ⒪"), bstack11lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭⒫"), bstack11lll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ⒬"), bstack11lll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ⒭"), bstack11lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ⒮"), bstack11lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪ⒯"), bstack11lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧ⒰")]:
        return
    node = store[bstack11lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⒱")]
    if hook_name in [bstack11lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭⒲"), bstack11lll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ⒳")]:
        node = store[bstack11lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡱࡴࡪࡵ࡭ࡧࡢ࡭ࡹ࡫࡭ࠨ⒴")]
    elif hook_name in [bstack11lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ⒵"), bstack11lll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬⒶ")]:
        node = store[bstack11lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪⒷ")]
    hook_type = bstack11l111ll111_opy_(hook_name)
    if event == bstack11lll1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭Ⓒ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_[hook_type], bstack1llll11l111_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack1ll11ll1_opy_ = {
            bstack11lll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬⒹ"): uuid,
            bstack11lll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬⒺ"): bstack1l1111l1_opy_(),
            bstack11lll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧⒻ"): bstack11lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨⒼ"),
            bstack11lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧⒽ"): hook_type,
            bstack11lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨⒾ"): hook_name
        }
        store[bstack11lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪⒿ")].append(uuid)
        bstack1lll1llll111_opy_ = node.nodeid
        if hook_type == bstack11lll1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬⓀ"):
            if not _1l11l11l_opy_.get(bstack1lll1llll111_opy_, None):
                _1l11l11l_opy_[bstack1lll1llll111_opy_] = {bstack11lll1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧⓁ"): []}
            _1l11l11l_opy_[bstack1lll1llll111_opy_][bstack11lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨⓂ")].append(bstack1ll11ll1_opy_[bstack11lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨⓃ")])
        _1l11l11l_opy_[bstack1lll1llll111_opy_ + bstack11lll1_opy_ (u"ࠫ࠲࠭Ⓞ") + hook_name] = bstack1ll11ll1_opy_
        bstack1lll1ll1l11l_opy_(node, bstack1ll11ll1_opy_, bstack11lll1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭Ⓟ"))
    elif event == bstack11lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬⓆ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_[hook_type], bstack1llll11l111_opy_.POST, node, None, bstack1ll111ll11l_opy_)
            return
        bstack1l1lll11_opy_ = node.nodeid + bstack11lll1_opy_ (u"ࠧ࠮ࠩⓇ") + hook_name
        _1l11l11l_opy_[bstack1l1lll11_opy_][bstack11lll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭Ⓢ")] = bstack1l1111l1_opy_()
        bstack1lll1lll1111_opy_(_1l11l11l_opy_[bstack1l1lll11_opy_][bstack11lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧⓉ")])
        bstack1lll1ll1l11l_opy_(node, _1l11l11l_opy_[bstack1l1lll11_opy_], bstack11lll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬⓊ"), bstack1lll1ll1l1l1_opy_=bstack1ll111ll11l_opy_)
def bstack1lll1lllllll_opy_():
    global bstack1lll1ll1ll11_opy_
    if bstack1lll1ll11l_opy_():
        bstack1lll1ll1ll11_opy_ = bstack11lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨⓋ")
    else:
        bstack1lll1ll1ll11_opy_ = bstack11lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬⓌ")
@bstack1ll1l11l_opy_.bstack1llll11l1l1l_opy_
def bstack1lll1ll11ll1_opy_():
    bstack1lll1lllllll_opy_()
    if cli.is_running():
        try:
            bstack11l1l1ll11l_opy_(bstack1lll1ll1ll1l_opy_)
        except Exception as e:
            logger.debug(bstack11lll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡶࠤࡵࡧࡴࡤࡪ࠽ࠤࢀࢃࠢⓍ").format(e))
        return
    if bstack1111l1l11l_opy_():
        bstack1lll1l11l_opy_ = Config.bstack111ll1l1_opy_()
        bstack11lll1_opy_ (u"ࠧࠨࠩࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡈࡲࡶࠥࡶࡰࡱࠢࡀࠤ࠶࠲ࠠ࡮ࡱࡧࡣࡪࡾࡥࡤࡷࡷࡩࠥ࡭ࡥࡵࡵࠣࡹࡸ࡫ࡤࠡࡨࡲࡶࠥࡧ࠱࠲ࡻࠣࡧࡴࡳ࡭ࡢࡰࡧࡷ࠲ࡽࡲࡢࡲࡳ࡭ࡳ࡭ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡌ࡯ࡳࠢࡳࡴࡵࠦ࠾ࠡ࠳࠯ࠤࡲࡵࡤࡠࡧࡻࡩࡨࡻࡴࡦࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡤࡨࡧࡦࡻࡳࡦࠢ࡬ࡸࠥ࡯ࡳࠡࡲࡤࡸࡨ࡮ࡥࡥࠢ࡬ࡲࠥࡧࠠࡥ࡫ࡩࡪࡪࡸࡥ࡯ࡶࠣࡴࡷࡵࡣࡦࡵࡶࠤ࡮ࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡶࡵࠣࡻࡪࠦ࡮ࡦࡧࡧࠤࡹࡵࠠࡶࡵࡨࠤࡘ࡫࡬ࡦࡰ࡬ࡹࡲࡖࡡࡵࡥ࡫ࠬࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡨࡢࡰࡧࡰࡪࡸࠩࠡࡨࡲࡶࠥࡶࡰࡱࠢࡁࠤ࠶ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨࠩࠪⓎ")
        if bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬⓏ")):
            if CONFIG.get(bstack11lll1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩⓐ")) is not None and int(CONFIG[bstack11lll1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪⓑ")]) > 1:
                bstack111ll1ll1l_opy_(bstack11l1lll1l1_opy_)
            return
        bstack111ll1ll1l_opy_(bstack11l1lll1l1_opy_)
    try:
        bstack11l1l1ll11l_opy_(bstack1lll1ll1ll1l_opy_)
    except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡴࠢࡳࡥࡹࡩࡨ࠻ࠢࡾࢁࠧⓒ").format(e))
bstack1lll1ll11ll1_opy_()