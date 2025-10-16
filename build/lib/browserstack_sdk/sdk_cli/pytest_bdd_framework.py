# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1ll1ll1llll_opy_
from browserstack_sdk.sdk_cli.utils.bstack1l1ll1l11_opy_ import bstack1ll11l1ll11_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l1ll1l_opy_,
    bstack1llll1l1l11_opy_,
    bstack1lll1llll1l_opy_,
    bstack1ll11l111ll_opy_,
    bstack1ll111l1l1l_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll111l11l1_opy_
from bstack_utils.bstack1lll11ll11_opy_ import bstack1llll1l1lll_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1l1lllll111_opy_ import bstack1ll11l111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll1l1111l_opy_
bstack1ll11ll1l1l_opy_ = bstack1ll111l11l1_opy_()
bstack1ll111ll111_opy_ = bstack1l_opy_ (u"࡚ࠦࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠰ࠦᇻ")
bstack1ll11l11lll_opy_ = bstack1l_opy_ (u"ࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠣᇼ")
bstack1ll1111llll_opy_ = bstack1l_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠧᇽ")
bstack1l1llllllll_opy_ = 1.0
_1ll11l1l1ll_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll1l11l11l_opy_ = bstack1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᇾ")
    bstack1ll11l11l11_opy_ = bstack1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࠨᇿ")
    bstack1ll11l11l1l_opy_ = bstack1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣሀ")
    bstack1ll11l11ll1_opy_ = bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࠧሁ")
    bstack1ll11l1l11l_opy_ = bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢሂ")
    bstack1ll1111l111_opy_: bool
    bstack1lll1l11111_opy_: bstack1lll1l1111l_opy_  = None
    bstack1ll1l1ll1l1_opy_ = [
        bstack1lll1l1ll1l_opy_.BEFORE_ALL,
        bstack1lll1l1ll1l_opy_.AFTER_ALL,
        bstack1lll1l1ll1l_opy_.BEFORE_EACH,
        bstack1lll1l1ll1l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11ll11l1_opy_: Dict[str, str],
        bstack1ll11l1llll_opy_: List[str]=[bstack1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤሃ")],
        bstack1lll1l11111_opy_: bstack1lll1l1111l_opy_ = None,
        bstack1llll1lll1l_opy_=None
    ):
        super().__init__(bstack1ll11l1llll_opy_, bstack1ll11ll11l1_opy_, bstack1lll1l11111_opy_)
        self.bstack1ll1111l111_opy_ = any(bstack1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥሄ") in item.lower() for item in bstack1ll11l1llll_opy_)
        self.bstack1llll1lll1l_opy_ = bstack1llll1lll1l_opy_
    def track_event(
        self,
        context: bstack1ll11l111ll_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        test_hook_state: bstack1lll1llll1l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l1ll1l_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll1l1ll1l1_opy_:
            bstack1ll11l1ll11_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l1ll1l_opy_.NONE:
            self.logger.warning(bstack1l_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫ࡤࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࠣህ") + str(test_hook_state) + bstack1l_opy_ (u"ࠣࠤሆ"))
            return
        if not self.bstack1ll1111l111_opy_:
            self.logger.warning(bstack1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠿ࠥሇ") + str(str(self.bstack1ll11l1llll_opy_)) + bstack1l_opy_ (u"ࠥࠦለ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨሉ") + str(kwargs) + bstack1l_opy_ (u"ࠧࠨሊ"))
            return
        instance = self.__1ll11111l1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡡࡳࡩࡶࡁࠧላ") + str(args) + bstack1l_opy_ (u"ࠢࠣሌ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1ll1l1_opy_ and test_hook_state == bstack1lll1llll1l_opy_.PRE:
                bstack1ll1l1lll11_opy_ = bstack1llll1l1lll_opy_.bstack1ll11llllll_opy_(EVENTS.bstack1lll11l1l_opy_.value)
                name = str(EVENTS.bstack1lll11l1l_opy_.name)+bstack1l_opy_ (u"ࠣ࠼ࠥል")+str(test_framework_state.name)
                TestFramework.bstack1ll1111ll11_opy_(instance, name, bstack1ll1l1lll11_opy_)
        except Exception as e:
            self.logger.debug(bstack1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶࠥࡶࡲࡦ࠼ࠣࡿࢂࠨሎ").format(e))
        try:
            if test_framework_state == bstack1lll1l1ll1l_opy_.TEST:
                if not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l1111ll_opy_) and test_hook_state == bstack1lll1llll1l_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll1l111l1l_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1l_opy_ (u"ࠥࡰࡴࡧࡤࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥሏ") + str(test_hook_state) + bstack1l_opy_ (u"ࠦࠧሐ"))
                if test_hook_state == bstack1lll1llll1l_opy_.PRE and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll11l1l1l1_opy_):
                    TestFramework.bstack1lllll11ll1_opy_(instance, TestFramework.bstack1ll11l1l1l1_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll1l11llll_opy_(instance, args)
                    self.logger.debug(bstack1l_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡴࡶࡤࡶࡹࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥሑ") + str(test_hook_state) + bstack1l_opy_ (u"ࠨࠢሒ"))
                elif test_hook_state == bstack1lll1llll1l_opy_.POST and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1ll11111_opy_):
                    TestFramework.bstack1lllll11ll1_opy_(instance, TestFramework.bstack1ll1ll11111_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡨࡲࡩࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥሓ") + str(test_hook_state) + bstack1l_opy_ (u"ࠣࠤሔ"))
            elif test_framework_state == bstack1lll1l1ll1l_opy_.STEP:
                if test_hook_state == bstack1lll1llll1l_opy_.PRE:
                    PytestBDDFramework.__1ll1ll11l1l_opy_(instance, args)
                elif test_hook_state == bstack1lll1llll1l_opy_.POST:
                    PytestBDDFramework.__1ll11111ll1_opy_(instance, args)
            elif test_framework_state == bstack1lll1l1ll1l_opy_.LOG and test_hook_state == bstack1lll1llll1l_opy_.POST:
                PytestBDDFramework.__1ll1l1111l1_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l1ll1l_opy_.LOG_REPORT and test_hook_state == bstack1lll1llll1l_opy_.POST:
                self.__1ll11lll11l_opy_(instance, *args)
                self.__1ll1l11ll11_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll1l1ll1l1_opy_:
                self.__1ll1l1l1111_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥሕ") + str(instance.ref()) + bstack1l_opy_ (u"ࠥࠦሖ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1111ll1l_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1ll1l1_opy_ and test_hook_state == bstack1lll1llll1l_opy_.POST:
                name = str(EVENTS.bstack1lll11l1l_opy_.name)+bstack1l_opy_ (u"ࠦ࠿ࠨሗ")+str(test_framework_state.name)
                bstack1ll1l1lll11_opy_ = TestFramework.bstack1ll11llll1l_opy_(instance, name)
                bstack1llll1l1lll_opy_.end(EVENTS.bstack1lll11l1l_opy_.value, bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧመ"), bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦሙ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢሚ").format(e))
    def bstack1ll111lll11_opy_(self):
        return self.bstack1ll1111l111_opy_
    def __1ll11l1111l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧማ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l1l1ll1_opy_(rep, [bstack1l_opy_ (u"ࠤࡺ࡬ࡪࡴࠢሜ"), bstack1l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦም"), bstack1l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦሞ"), bstack1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧሟ"), bstack1l_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠢሠ"), bstack1l_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨሡ")])
        return None
    def __1ll11lll11l_opy_(self, instance: bstack1llll1l1l11_opy_, *args):
        result = self.__1ll11l1111l_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l11ll_opy_ = None
        if result.get(bstack1l_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤሢ"), None) == bstack1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤሣ") and len(args) > 1 and getattr(args[1], bstack1l_opy_ (u"ࠥࡩࡽࡩࡩ࡯ࡨࡲࠦሤ"), None) is not None:
            failure = [{bstack1l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧሥ"): [args[1].excinfo.exconly(), result.get(bstack1l_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦሦ"), None)]}]
            bstack11111l11ll_opy_ = bstack1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢሧ") if bstack1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥረ") in getattr(args[1].excinfo, bstack1l_opy_ (u"ࠣࡶࡼࡴࡪࡴࡡ࡮ࡧࠥሩ"), bstack1l_opy_ (u"ࠤࠥሪ")) else bstack1l_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦራ")
        bstack1ll1111l1l1_opy_ = result.get(bstack1l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧሬ"), TestFramework.bstack1ll111l1l11_opy_)
        if bstack1ll1111l1l1_opy_ != TestFramework.bstack1ll111l1l11_opy_:
            TestFramework.bstack1lllll11ll1_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11111111_opy_(instance, {
            TestFramework.bstack1lll1lll1l1_opy_: failure,
            TestFramework.bstack1ll1l1ll111_opy_: bstack11111l11ll_opy_,
            TestFramework.bstack1lll1ll1lll_opy_: bstack1ll1111l1l1_opy_,
        })
    def __1ll11111l1l_opy_(
        self,
        context: bstack1ll11l111ll_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        test_hook_state: bstack1lll1llll1l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l1ll1l_opy_.SETUP_FIXTURE:
            instance = self.__1ll11ll111l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11ll11ll_opy_ bstack1ll1l11ll1l_opy_ this to be bstack1l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧር")
            if test_framework_state == bstack1lll1l1ll1l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l11l1ll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l1ll1l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l_opy_ (u"ࠨ࡮ࡰࡦࡨࠦሮ"), None), bstack1l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢሯ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l_opy_ (u"ࠣࡰࡲࡨࡪࠨሰ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤሱ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11ll1ll1_opy_(target) if target else None
        return instance
    def __1ll1l1l1111_opy_(
        self,
        instance: bstack1llll1l1l11_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        test_hook_state: bstack1lll1llll1l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1111lll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11l11l11_opy_, {})
        if not key in bstack1ll1111lll1_opy_:
            bstack1ll1111lll1_opy_[key] = []
        bstack1l1llllll11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11l11l1l_opy_, {})
        if not key in bstack1l1llllll11_opy_:
            bstack1l1llllll11_opy_[key] = []
        bstack1ll11lll1l1_opy_ = {
            PytestBDDFramework.bstack1ll11l11l11_opy_: bstack1ll1111lll1_opy_,
            PytestBDDFramework.bstack1ll11l11l1l_opy_: bstack1l1llllll11_opy_,
        }
        if test_hook_state == bstack1lll1llll1l_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1l_opy_ (u"ࠥ࡯ࡪࡿࠢሲ"): key,
                TestFramework.bstack1ll1l1llll1_opy_: uuid4().__str__(),
                TestFramework.bstack1ll1l11l1l1_opy_: TestFramework.bstack1ll111lllll_opy_,
                TestFramework.bstack1ll1l111lll_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1l1lll1l_opy_: [],
                TestFramework.bstack1ll11llll11_opy_: hook_name,
                TestFramework.bstack1ll11ll1lll_opy_: bstack1ll11l111l1_opy_.bstack1ll11lllll1_opy_()
            }
            bstack1ll1111lll1_opy_[key].append(hook)
            bstack1ll11lll1l1_opy_[PytestBDDFramework.bstack1ll11l11ll1_opy_] = key
        elif test_hook_state == bstack1lll1llll1l_opy_.POST:
            bstack1ll111l111l_opy_ = bstack1ll1111lll1_opy_.get(key, [])
            hook = bstack1ll111l111l_opy_.pop() if bstack1ll111l111l_opy_ else None
            if hook:
                result = self.__1ll11l1111l_opy_(*args)
                if result:
                    bstack1ll1l1l1lll_opy_ = result.get(bstack1l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧሳ"), TestFramework.bstack1ll111lllll_opy_)
                    if bstack1ll1l1l1lll_opy_ != TestFramework.bstack1ll111lllll_opy_:
                        hook[TestFramework.bstack1ll1l11l1l1_opy_] = bstack1ll1l1l1lll_opy_
                hook[TestFramework.bstack1ll111111ll_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11ll1lll_opy_] = bstack1ll11l111l1_opy_.bstack1ll11lllll1_opy_()
                self.bstack1l1llll1lll_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1l111l11_opy_, [])
                self.bstack1ll1111l11l_opy_(instance, logs)
                bstack1l1llllll11_opy_[key].append(hook)
                bstack1ll11lll1l1_opy_[PytestBDDFramework.bstack1ll11l1l11l_opy_] = key
        TestFramework.bstack1ll11111111_opy_(instance, bstack1ll11lll1l1_opy_)
        self.logger.debug(bstack1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡭ࡵ࡯࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡱࡥࡺࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪ࠽ࡼࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡾࠢ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡀࠦሴ") + str(bstack1l1llllll11_opy_) + bstack1l_opy_ (u"ࠨࠢስ"))
    def __1ll11ll111l_opy_(
        self,
        context: bstack1ll11l111ll_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        test_hook_state: bstack1lll1llll1l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l1l1ll1_opy_(args[0], [bstack1l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨሶ"), bstack1l_opy_ (u"ࠣࡣࡵ࡫ࡳࡧ࡭ࡦࠤሷ"), bstack1l_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤሸ"), bstack1l_opy_ (u"ࠥ࡭ࡩࡹࠢሹ"), bstack1l_opy_ (u"ࠦࡺࡴࡩࡵࡶࡨࡷࡹࠨሺ"), bstack1l_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧሻ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧሼ")) else fixturedef.get(bstack1l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨሽ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨሾ")) else None
        node = request.node if hasattr(request, bstack1l_opy_ (u"ࠤࡱࡳࡩ࡫ࠢሿ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥቀ")) else None
        baseid = fixturedef.get(bstack1l_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦቁ"), None) or bstack1l_opy_ (u"ࠧࠨቂ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l_opy_ (u"ࠨ࡟ࡱࡻࡩࡹࡳࡩࡩࡵࡧࡰࠦቃ")):
            target = PytestBDDFramework.__1ll1l1l11ll_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l_opy_ (u"ࠢ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤቄ")) else None
            if target and not TestFramework.bstack1ll11ll1ll1_opy_(target):
                self.__1ll1l11l1ll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡲࡴࡪࡥ࠾ࡽࡱࡳࡩ࡫ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥቅ") + str(test_hook_state) + bstack1l_opy_ (u"ࠤࠥቆ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣቇ") + str(target) + bstack1l_opy_ (u"ࠦࠧቈ"))
            return None
        instance = TestFramework.bstack1ll11ll1ll1_opy_(target)
        if not instance:
            self.logger.warning(bstack1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡧࡧࡳࡦ࡫ࡧࡁࢀࡨࡡࡴࡧ࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢ቉") + str(target) + bstack1l_opy_ (u"ࠨࠢቊ"))
            return None
        bstack1ll11l1lll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l11l11l_opy_, {})
        if os.getenv(bstack1l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡆࡊ࡚ࡗ࡙ࡗࡋࡓࠣቋ"), bstack1l_opy_ (u"ࠣ࠳ࠥቌ")) == bstack1l_opy_ (u"ࠤ࠴ࠦቍ"):
            bstack1ll1l1l1l11_opy_ = bstack1l_opy_ (u"ࠥ࠾ࠧ቎").join((scope, fixturename))
            bstack1ll1l1ll11l_opy_ = datetime.now(tz=timezone.utc)
            bstack1l1lllll1ll_opy_ = {
                bstack1l_opy_ (u"ࠦࡰ࡫ࡹࠣ቏"): bstack1ll1l1l1l11_opy_,
                bstack1l_opy_ (u"ࠧࡺࡡࡨࡵࠥቐ"): PytestBDDFramework.__1ll11lll111_opy_(request.node, scenario),
                bstack1l_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࠢቑ"): fixturedef,
                bstack1l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨቒ"): scope,
                bstack1l_opy_ (u"ࠣࡶࡼࡴࡪࠨቓ"): None,
            }
            try:
                if test_hook_state == bstack1lll1llll1l_opy_.POST and callable(getattr(args[-1], bstack1l_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨቔ"), None)):
                    bstack1l1lllll1ll_opy_[bstack1l_opy_ (u"ࠥࡸࡾࡶࡥࠣቕ")] = TestFramework.bstack1ll1l111111_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1llll1l_opy_.PRE:
                bstack1l1lllll1ll_opy_[bstack1l_opy_ (u"ࠦࡺࡻࡩࡥࠤቖ")] = uuid4().__str__()
                bstack1l1lllll1ll_opy_[PytestBDDFramework.bstack1ll1l111lll_opy_] = bstack1ll1l1ll11l_opy_
            elif test_hook_state == bstack1lll1llll1l_opy_.POST:
                bstack1l1lllll1ll_opy_[PytestBDDFramework.bstack1ll111111ll_opy_] = bstack1ll1l1ll11l_opy_
            if bstack1ll1l1l1l11_opy_ in bstack1ll11l1lll1_opy_:
                bstack1ll11l1lll1_opy_[bstack1ll1l1l1l11_opy_].update(bstack1l1lllll1ll_opy_)
                self.logger.debug(bstack1l_opy_ (u"ࠧࡻࡰࡥࡣࡷࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࠨ቗") + str(bstack1ll11l1lll1_opy_[bstack1ll1l1l1l11_opy_]) + bstack1l_opy_ (u"ࠨࠢቘ"))
            else:
                bstack1ll11l1lll1_opy_[bstack1ll1l1l1l11_opy_] = bstack1l1lllll1ll_opy_
                self.logger.debug(bstack1l_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࢁࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࢂࠦࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࠥ቙") + str(len(bstack1ll11l1lll1_opy_)) + bstack1l_opy_ (u"ࠣࠤቚ"))
        TestFramework.bstack1lllll11ll1_opy_(instance, PytestBDDFramework.bstack1ll1l11l11l_opy_, bstack1ll11l1lll1_opy_)
        self.logger.debug(bstack1l_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࡿࡱ࡫࡮ࠩࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶ࠭ࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤቛ") + str(instance.ref()) + bstack1l_opy_ (u"ࠥࠦቜ"))
        return instance
    def __1ll1l11l1ll_opy_(
        self,
        context: bstack1ll11l111ll_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll1llll_opy_.create_context(target)
        ob = bstack1llll1l1l11_opy_(ctx, self.bstack1ll11l1llll_opy_, self.bstack1ll11ll11l1_opy_, test_framework_state)
        TestFramework.bstack1ll11111111_opy_(ob, {
            TestFramework.bstack1llll11111l_opy_: context.test_framework_name,
            TestFramework.bstack1llll1111l1_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l11111l_opy_: [],
            PytestBDDFramework.bstack1ll1l11l11l_opy_: {},
            PytestBDDFramework.bstack1ll11l11l1l_opy_: {},
            PytestBDDFramework.bstack1ll11l11l11_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllll11ll1_opy_(ob, TestFramework.bstack1ll111l1ll1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllll11ll1_opy_(ob, TestFramework.bstack1llll1lllll_opy_, context.platform_index)
        TestFramework.bstack1llll11l1ll_opy_[ctx.id] = ob
        self.logger.debug(bstack1l_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡩࡴࡹ࠰࡬ࡨࡂࢁࡣࡵࡺ࠱࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦቝ") + str(TestFramework.bstack1llll11l1ll_opy_.keys()) + bstack1l_opy_ (u"ࠧࠨ቞"))
        return ob
    @staticmethod
    def __1ll1l11llll_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l_opy_ (u"࠭ࡩࡥࠩ቟"): id(step),
                bstack1l_opy_ (u"ࠧࡵࡧࡻࡸࠬበ"): step.name,
                bstack1l_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩቡ"): step.keyword,
            })
        meta = {
            bstack1l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪቢ"): {
                bstack1l_opy_ (u"ࠪࡲࡦࡳࡥࠨባ"): feature.name,
                bstack1l_opy_ (u"ࠫࡵࡧࡴࡩࠩቤ"): feature.filename,
                bstack1l_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪብ"): feature.description
            },
            bstack1l_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨቦ"): {
                bstack1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬቧ"): scenario.name
            },
            bstack1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧቨ"): steps,
            bstack1l_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫቩ"): PytestBDDFramework.__1ll1111111l_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll111l11ll_opy_: meta
            }
        )
    def bstack1l1llll1lll_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡴࡲࡧࡪࡹࡳࡦࡵࠣࡸ࡭࡫ࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡵ࡬ࡱ࡮ࡲࡡࡳࠢࡷࡳࠥࡺࡨࡦࠢࡍࡥࡻࡧࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡯ࡳࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡄࡪࡨࡧࡰࡹࠠࡵࡪࡨࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࡭ࡳࡹࡩࡥࡧࠣࢂ࠴࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠴࡛ࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡊࡴࡸࠠࡦࡣࡦ࡬ࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡨࡰࡱ࡮ࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠮ࠣࡶࡪࡶ࡬ࡢࡥࡨࡷࠥࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧࠦࡩ࡯ࠢ࡬ࡸࡸࠦࡰࡢࡶ࡫࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡍ࡫ࠦࡡࠡࡨ࡬ࡰࡪࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡰࡥࡹࡩࡨࡦࡵࠣࡥࠥࡳ࡯ࡥ࡫ࡩ࡭ࡪࡪࠠࡩࡱࡲ࡯࠲ࡲࡥࡷࡧ࡯ࠤ࡫࡯࡬ࡦ࠮ࠣ࡭ࡹࠦࡣࡳࡧࡤࡸࡪࡹࠠࡢࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࠤࡼ࡯ࡴࡩࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡤࡦࡶࡤ࡭ࡱࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡓࡪ࡯࡬ࡰࡦࡸ࡬ࡺ࠮ࠣ࡭ࡹࠦࡰࡳࡱࡦࡩࡸࡹࡥࡴࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡱࡵࡣࡢࡶࡨࡨࠥ࡯࡮ࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯࠳ࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡦࡾࠦࡲࡦࡲ࡯ࡥࡨ࡯࡮ࡨࠢࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢࠡࡹ࡬ࡸ࡭ࠦࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡗ࡬ࡪࠦࡣࡳࡧࡤࡸࡪࡪࠠࡍࡱࡪࡉࡳࡺࡲࡺࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡥࡷ࡫ࠠࡢࡦࡧࡩࡩࠦࡴࡰࠢࡷ࡬ࡪࠦࡨࡰࡱ࡮ࠫࡸࠦࠢ࡭ࡱࡪࡷࠧࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡬ࡴࡵ࡫࠻ࠢࡗ࡬ࡪࠦࡥࡷࡧࡱࡸࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡ࡮ࡲ࡫ࡸࠦࡡ࡯ࡦࠣ࡬ࡴࡵ࡫ࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡔࡦࡺࡨࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤ࡙࡫ࡳࡵࡎࡨࡺࡪࡲࠠ࡮ࡱࡱ࡭ࡹࡵࡲࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡺ࡯࡬ࡥࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠠ࡮ࡱࡱ࡭ࡹࡵࡲࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤቪ")
        global _1ll11l1l1ll_opy_
        platform_index = os.environ[bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫቫ")]
        bstack1ll1l1l11l1_opy_ = os.path.join(bstack1ll11ll1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), bstack1ll11l11lll_opy_)
        if not os.path.exists(bstack1ll1l1l11l1_opy_) or not os.path.isdir(bstack1ll1l1l11l1_opy_):
            return
        logs = hook.get(bstack1l_opy_ (u"ࠧࡲ࡯ࡨࡵࠥቬ"), [])
        with os.scandir(bstack1ll1l1l11l1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11l1l1ll_opy_:
                    self.logger.info(bstack1l_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦቭ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1l_opy_ (u"ࠢࠣቮ")
                    log_entry = bstack1ll111l1l1l_opy_(
                        kind=bstack1l_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥቯ"),
                        message=bstack1l_opy_ (u"ࠤࠥተ"),
                        level=bstack1l_opy_ (u"ࠥࠦቱ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll111ll1l1_opy_=entry.stat().st_size,
                        bstack1ll1l11l111_opy_=bstack1l_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦቲ"),
                        bstack1ll11l1_opy_=os.path.abspath(entry.path),
                        bstack1l1lllll11l_opy_=hook.get(TestFramework.bstack1ll1l1llll1_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11l1l1ll_opy_.add(abs_path)
        platform_index = os.environ[bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬታ")]
        bstack1l1llllll1l_opy_ = os.path.join(bstack1ll11ll1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), bstack1ll11l11lll_opy_, bstack1ll1111llll_opy_)
        if not os.path.exists(bstack1l1llllll1l_opy_) or not os.path.isdir(bstack1l1llllll1l_opy_):
            self.logger.info(bstack1l_opy_ (u"ࠨࡎࡰࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡩࡳࡺࡴࡤࠡࡣࡷ࠾ࠥࢁࡽࠣቴ").format(bstack1l1llllll1l_opy_))
        else:
            self.logger.info(bstack1l_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡨࡵࡳࡲࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠼ࠣࡿࢂࠨት").format(bstack1l1llllll1l_opy_))
            with os.scandir(bstack1l1llllll1l_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11l1l1ll_opy_:
                        self.logger.info(bstack1l_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨቶ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1l_opy_ (u"ࠤࠥቷ")
                        log_entry = bstack1ll111l1l1l_opy_(
                            kind=bstack1l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧቸ"),
                            message=bstack1l_opy_ (u"ࠦࠧቹ"),
                            level=bstack1l_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤቺ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll111ll1l1_opy_=entry.stat().st_size,
                            bstack1ll1l11l111_opy_=bstack1l_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨቻ"),
                            bstack1ll11l1_opy_=os.path.abspath(entry.path),
                            bstack1ll11ll1l11_opy_=hook.get(TestFramework.bstack1ll1l1llll1_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11l1l1ll_opy_.add(abs_path)
        hook[bstack1l_opy_ (u"ࠢ࡭ࡱࡪࡷࠧቼ")] = logs
    def bstack1ll1111l11l_opy_(
        self,
        bstack1l1lllll1l1_opy_: bstack1llll1l1l11_opy_,
        entries: List[bstack1ll111l1l1l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡕࡈࡗࡘࡏࡏࡏࡡࡌࡈࠧች"))
        req.platform_index = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll1lllll_opy_)
        req.execution_context.hash = str(bstack1l1lllll1l1_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1lllll1l1_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1lllll1l1_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll11111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.uuid = entry.bstack1l1lllll11l_opy_ if entry.bstack1l1lllll11l_opy_ else TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll11ll11_opy_)
            log_entry.test_framework_state = bstack1l1lllll1l1_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣቾ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧቿ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll111ll1l1_opy_
                log_entry.file_path = entry.bstack1ll11l1_opy_
        def bstack1ll1l1l1l1l_opy_():
            bstack1l1111lll_opy_ = datetime.now()
            try:
                self.bstack1llll1lll1l_opy_.LogCreatedEvent(req)
                bstack1l1lllll1l1_opy_.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠣኀ"), datetime.now() - bstack1l1111lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡽࢀࠦኁ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll1l11111_opy_.enqueue(bstack1ll1l1l1l1l_opy_)
    def __1ll1l11ll11_opy_(self, instance) -> None:
        bstack1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡐࡴࡧࡤࡴࠢࡦࡹࡸࡺ࡯࡮ࠢࡷࡥ࡬ࡹࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡩ࡬ࡺࡪࡴࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡲࡦࡣࡷࡩࡸࠦࡡࠡࡦ࡬ࡧࡹࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣࡸࡪࡹࡴࠡ࡮ࡨࡺࡪࡲࠠࡤࡷࡶࡸࡴࡳࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡵࡩࡹࡸࡩࡦࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡻࡳࡵࡱࡰࡘࡦ࡭ࡍࡢࡰࡤ࡫ࡪࡸࠠࡢࡰࡧࠤࡺࡶࡤࡢࡶࡨࡷࠥࡺࡨࡦࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡸࡺࡡࡵࡧࠣࡹࡸ࡯࡮ࡨࠢࡶࡩࡹࡥࡳࡵࡣࡷࡩࡤ࡫࡮ࡵࡴ࡬ࡩࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦኂ")
        bstack1ll11lll1l1_opy_ = {bstack1l_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠤኃ"): bstack1ll11l111l1_opy_.bstack1ll11lllll1_opy_()}
        TestFramework.bstack1ll11111111_opy_(instance, bstack1ll11lll1l1_opy_)
    @staticmethod
    def __1ll1ll11l1l_opy_(instance, args):
        request, bstack1ll1ll1111l_opy_ = args
        bstack1l1lllllll1_opy_ = id(bstack1ll1ll1111l_opy_)
        bstack1ll1ll111ll_opy_ = instance.data[TestFramework.bstack1ll111l11ll_opy_]
        step = next(filter(lambda st: st[bstack1l_opy_ (u"ࠨ࡫ࡧࠫኄ")] == bstack1l1lllllll1_opy_, bstack1ll1ll111ll_opy_[bstack1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኅ")]), None)
        step.update({
            bstack1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧኆ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll1ll111ll_opy_[bstack1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኇ")]) if st[bstack1l_opy_ (u"ࠬ࡯ࡤࠨኈ")] == step[bstack1l_opy_ (u"࠭ࡩࡥࠩ኉")]), None)
        if index is not None:
            bstack1ll1ll111ll_opy_[bstack1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኊ")][index] = step
        instance.data[TestFramework.bstack1ll111l11ll_opy_] = bstack1ll1ll111ll_opy_
    @staticmethod
    def __1ll11111ll1_opy_(instance, args):
        bstack1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡽࡨࡦࡰࠣࡰࡪࡴࠠࡢࡴࡪࡷࠥ࡯ࡳࠡ࠴࠯ࠤ࡮ࡺࠠࡴ࡫ࡪࡲ࡮࡬ࡩࡦࡵࠣࡸ࡭࡫ࡲࡦࠢ࡬ࡷࠥࡴ࡯ࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡶ࡬ࡹࠠࡢࡴࡨࠤ࠲࡛ࠦࡳࡧࡴࡹࡪࡹࡴ࠭ࠢࡶࡸࡪࡶ࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡪࠥࡧࡲࡨࡵࠣࡥࡷ࡫ࠠ࠴ࠢࡷ࡬ࡪࡴࠠࡵࡪࡨࠤࡱࡧࡳࡵࠢࡹࡥࡱࡻࡥࠡ࡫ࡶࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦኋ")
        bstack1ll1l1lllll_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll1ll1111l_opy_ = args[1]
        bstack1l1lllllll1_opy_ = id(bstack1ll1ll1111l_opy_)
        bstack1ll1ll111ll_opy_ = instance.data[TestFramework.bstack1ll111l11ll_opy_]
        step = None
        if bstack1l1lllllll1_opy_ is not None and bstack1ll1ll111ll_opy_.get(bstack1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኌ")):
            step = next(filter(lambda st: st[bstack1l_opy_ (u"ࠪ࡭ࡩ࠭ኍ")] == bstack1l1lllllll1_opy_, bstack1ll1ll111ll_opy_[bstack1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ኎")]), None)
            step.update({
                bstack1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ኏"): bstack1ll1l1lllll_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ነ"): bstack1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧኑ"),
                bstack1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩኒ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩና"): bstack1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪኔ"),
                })
        index = next((i for i, st in enumerate(bstack1ll1ll111ll_opy_[bstack1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪን")]) if st[bstack1l_opy_ (u"ࠬ࡯ࡤࠨኖ")] == step[bstack1l_opy_ (u"࠭ࡩࡥࠩኗ")]), None)
        if index is not None:
            bstack1ll1ll111ll_opy_[bstack1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኘ")][index] = step
        instance.data[TestFramework.bstack1ll111l11ll_opy_] = bstack1ll1ll111ll_opy_
    @staticmethod
    def __1ll1111111l_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1l_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪኙ")):
                examples = list(node.callspec.params[bstack1l_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨኚ")].values())
            return examples
        except:
            return []
    def bstack1ll1l111ll1_opy_(self, instance: bstack1llll1l1l11_opy_, bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_]):
        bstack1ll111l1lll_opy_ = (
            PytestBDDFramework.bstack1ll11l11ll1_opy_
            if bstack1lllll1ll11_opy_[1] == bstack1lll1llll1l_opy_.PRE
            else PytestBDDFramework.bstack1ll11l1l11l_opy_
        )
        hook = PytestBDDFramework.bstack1ll11l1ll1l_opy_(instance, bstack1ll111l1lll_opy_)
        entries = hook.get(TestFramework.bstack1ll1l1lll1l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l11111l_opy_, []))
        return entries
    def bstack1ll111llll1_opy_(self, instance: bstack1llll1l1l11_opy_, bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_]):
        bstack1ll111l1lll_opy_ = (
            PytestBDDFramework.bstack1ll11l11ll1_opy_
            if bstack1lllll1ll11_opy_[1] == bstack1lll1llll1l_opy_.PRE
            else PytestBDDFramework.bstack1ll11l1l11l_opy_
        )
        PytestBDDFramework.bstack1ll11l1l111_opy_(instance, bstack1ll111l1lll_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l11111l_opy_, []).clear()
    @staticmethod
    def bstack1ll11l1ll1l_opy_(instance: bstack1llll1l1l11_opy_, bstack1ll111l1lll_opy_: str):
        bstack1ll111l1111_opy_ = (
            PytestBDDFramework.bstack1ll11l11l1l_opy_
            if bstack1ll111l1lll_opy_ == PytestBDDFramework.bstack1ll11l1l11l_opy_
            else PytestBDDFramework.bstack1ll11l11l11_opy_
        )
        bstack1ll111111l1_opy_ = TestFramework.get_state(instance, bstack1ll111l1lll_opy_, None)
        bstack1ll1l1ll1ll_opy_ = TestFramework.get_state(instance, bstack1ll111l1111_opy_, None) if bstack1ll111111l1_opy_ else None
        return (
            bstack1ll1l1ll1ll_opy_[bstack1ll111111l1_opy_][-1]
            if isinstance(bstack1ll1l1ll1ll_opy_, dict) and len(bstack1ll1l1ll1ll_opy_.get(bstack1ll111111l1_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11l1l111_opy_(instance: bstack1llll1l1l11_opy_, bstack1ll111l1lll_opy_: str):
        hook = PytestBDDFramework.bstack1ll11l1ll1l_opy_(instance, bstack1ll111l1lll_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1l1lll1l_opy_, []).clear()
    @staticmethod
    def __1ll1l1111l1_opy_(instance: bstack1llll1l1l11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡦࡳࡷࡪࡳࠣኛ"), None)):
            return
        if os.getenv(bstack1l_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡐࡔࡍࡓࠣኜ"), bstack1l_opy_ (u"ࠧ࠷ࠢኝ")) != bstack1l_opy_ (u"ࠨ࠱ࠣኞ"):
            PytestBDDFramework.logger.warning(bstack1l_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡯࡮ࡨࠢࡦࡥࡵࡲ࡯ࡨࠤኟ"))
            return
        bstack1ll111lll1l_opy_ = {
            bstack1l_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢአ"): (PytestBDDFramework.bstack1ll11l11ll1_opy_, PytestBDDFramework.bstack1ll11l11l11_opy_),
            bstack1l_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦኡ"): (PytestBDDFramework.bstack1ll11l1l11l_opy_, PytestBDDFramework.bstack1ll11l11l1l_opy_),
        }
        for when in (bstack1l_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤኢ"), bstack1l_opy_ (u"ࠦࡨࡧ࡬࡭ࠤኣ"), bstack1l_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢኤ")):
            bstack1ll11ll1111_opy_ = args[1].get_records(when)
            if not bstack1ll11ll1111_opy_:
                continue
            records = [
                bstack1ll111l1l1l_opy_(
                    kind=TestFramework.bstack1ll11111l11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠤእ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫ࡤࠣኦ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11ll1111_opy_
                if isinstance(getattr(r, bstack1l_opy_ (u"ࠣ࡯ࡨࡷࡸࡧࡧࡦࠤኧ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll111ll1ll_opy_, bstack1ll111l1111_opy_ = bstack1ll111lll1l_opy_.get(when, (None, None))
            bstack1ll11111lll_opy_ = TestFramework.get_state(instance, bstack1ll111ll1ll_opy_, None) if bstack1ll111ll1ll_opy_ else None
            bstack1ll1l1ll1ll_opy_ = TestFramework.get_state(instance, bstack1ll111l1111_opy_, None) if bstack1ll11111lll_opy_ else None
            if isinstance(bstack1ll1l1ll1ll_opy_, dict) and len(bstack1ll1l1ll1ll_opy_.get(bstack1ll11111lll_opy_, [])) > 0:
                hook = bstack1ll1l1ll1ll_opy_[bstack1ll11111lll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1l1lll1l_opy_ in hook:
                    hook[TestFramework.bstack1ll1l1lll1l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l11111l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l111l1l_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1ll111l1_opy_(request.node, scenario)
        bstack1ll111ll11l_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll111ll11l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1llll11ll11_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l1111ll_opy_: test_id,
            TestFramework.bstack1ll1l11lll1_opy_: test_name,
            TestFramework.bstack1ll1111l1ll_opy_: test_id,
            TestFramework.bstack1ll11l11111_opy_: bstack1ll111ll11l_opy_,
            TestFramework.bstack1ll11lll1ll_opy_: PytestBDDFramework.__1ll11lll111_opy_(feature, scenario),
            TestFramework.bstack1ll1ll11l11_opy_: code,
            TestFramework.bstack1lll1ll1lll_opy_: TestFramework.bstack1ll111l1l11_opy_,
            TestFramework.bstack1lll11lll1l_opy_: test_name
        }
    @staticmethod
    def __1ll1ll111l1_opy_(node, scenario):
        if hasattr(node, bstack1l_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫከ")):
            parts = node.nodeid.rsplit(bstack1l_opy_ (u"ࠥ࡟ࠧኩ"))
            params = parts[-1]
            return bstack1l_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦኪ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll11lll111_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1l_opy_ (u"ࠬࡺࡡࡨࡵࠪካ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1l_opy_ (u"࠭ࡴࡢࡩࡶࠫኬ")) else [])
    @staticmethod
    def __1ll1l1l11ll_opy_(location):
        return bstack1l_opy_ (u"ࠢ࠻࠼ࠥክ").join(filter(lambda x: isinstance(x, str), location))