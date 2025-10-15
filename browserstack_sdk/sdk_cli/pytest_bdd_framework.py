# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1ll1lll111l_opy_
from browserstack_sdk.sdk_cli.utils.bstack1l1lll1ll1_opy_ import bstack1ll11ll1lll_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll11l1ll_opy_,
    bstack1lll1l1l1ll_opy_,
    bstack1lll1llll11_opy_,
    bstack1ll1l1lllll_opy_,
    bstack1ll11lll111_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll1l11ll11_opy_
from bstack_utils.bstack111l11llll_opy_ import bstack1llll1l1l11_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll111l1l1l_opy_ import bstack1l1lllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll1l11111_opy_
bstack1ll1111llll_opy_ = bstack1ll1l11ll11_opy_()
bstack1ll1l11lll1_opy_ = bstack1ll1l_opy_ (u"࡙ࠥࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠯ࠥᇳ")
bstack1ll11l1l1l1_opy_ = bstack1ll1l_opy_ (u"ࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢᇴ")
bstack1ll1111l1ll_opy_ = bstack1ll1l_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦᇵ")
bstack1ll1111ll1l_opy_ = 1.0
_1ll11l11111_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll1l1l11l1_opy_ = bstack1ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᇶ")
    bstack1ll11ll1l1l_opy_ = bstack1ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࠧᇷ")
    bstack1ll11111lll_opy_ = bstack1ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᇸ")
    bstack1ll111l1lll_opy_ = bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࠦᇹ")
    bstack1ll1l1111ll_opy_ = bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨᇺ")
    bstack1ll1l1lll1l_opy_: bool
    bstack1lll11lllll_opy_: bstack1lll1l11111_opy_  = None
    bstack1ll1111l11l_opy_ = [
        bstack1llll11l1ll_opy_.BEFORE_ALL,
        bstack1llll11l1ll_opy_.AFTER_ALL,
        bstack1llll11l1ll_opy_.BEFORE_EACH,
        bstack1llll11l1ll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l1llllll11_opy_: Dict[str, str],
        bstack1ll1ll111ll_opy_: List[str]=[bstack1ll1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣᇻ")],
        bstack1lll11lllll_opy_: bstack1lll1l11111_opy_ = None,
        bstack1llll1l1ll1_opy_=None
    ):
        super().__init__(bstack1ll1ll111ll_opy_, bstack1l1llllll11_opy_, bstack1lll11lllll_opy_)
        self.bstack1ll1l1lll1l_opy_ = any(bstack1ll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤᇼ") in item.lower() for item in bstack1ll1ll111ll_opy_)
        self.bstack1llll1l1ll1_opy_ = bstack1llll1l1ll1_opy_
    def track_event(
        self,
        context: bstack1ll1l1lllll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1lll1llll11_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll11l1ll_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll1111l11l_opy_:
            bstack1ll11ll1lll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll11l1ll_opy_.NONE:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࠢᇽ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠢࠣᇾ"))
            return
        if not self.bstack1ll1l1lll1l_opy_:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠾ࠤᇿ") + str(str(self.bstack1ll1ll111ll_opy_)) + bstack1ll1l_opy_ (u"ࠤࠥሀ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧሁ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠦࠧሂ"))
            return
        instance = self.__1ll1l111lll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࠦሃ") + str(args) + bstack1ll1l_opy_ (u"ࠨࠢሄ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1111l11l_opy_ and test_hook_state == bstack1lll1llll11_opy_.PRE:
                bstack1l1lllll111_opy_ = bstack1llll1l1l11_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack11ll11111l_opy_.value)
                name = str(EVENTS.bstack11ll11111l_opy_.name)+bstack1ll1l_opy_ (u"ࠢ࠻ࠤህ")+str(test_framework_state.name)
                TestFramework.bstack1ll1l1l1l11_opy_(instance, name, bstack1l1lllll111_opy_)
        except Exception as e:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵࠤࡵࡸࡥ࠻ࠢࡾࢁࠧሆ").format(e))
        try:
            if test_framework_state == bstack1llll11l1ll_opy_.TEST:
                if not TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1ll11l1llll_opy_) and test_hook_state == bstack1lll1llll11_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll1l1l1111_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1ll1l_opy_ (u"ࠤ࡯ࡳࡦࡪࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሇ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠥࠦለ"))
                if test_hook_state == bstack1lll1llll11_opy_.PRE and not TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1ll11l11l11_opy_):
                    TestFramework.bstack1111111ll1_opy_(instance, TestFramework.bstack1ll11l11l11_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll1l11llll_opy_(instance, args)
                    self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡳࡵࡣࡵࡸࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሉ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠧࠨሊ"))
                elif test_hook_state == bstack1lll1llll11_opy_.POST and not TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1ll11llllll_opy_):
                    TestFramework.bstack1111111ll1_opy_(instance, TestFramework.bstack1ll11llllll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡧࡱࡨࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤላ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠢࠣሌ"))
            elif test_framework_state == bstack1llll11l1ll_opy_.STEP:
                if test_hook_state == bstack1lll1llll11_opy_.PRE:
                    PytestBDDFramework.__1ll11lll11l_opy_(instance, args)
                elif test_hook_state == bstack1lll1llll11_opy_.POST:
                    PytestBDDFramework.__1ll11ll1111_opy_(instance, args)
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG and test_hook_state == bstack1lll1llll11_opy_.POST:
                PytestBDDFramework.__1l1llll1ll1_opy_(instance, *args)
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG_REPORT and test_hook_state == bstack1lll1llll11_opy_.POST:
                self.__1ll1l1111l1_opy_(instance, *args)
                self.__1ll11ll1ll1_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll1111l11l_opy_:
                self.__1ll11ll1l11_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤል") + str(instance.ref()) + bstack1ll1l_opy_ (u"ࠤࠥሎ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1l1llll1lll_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1111l11l_opy_ and test_hook_state == bstack1lll1llll11_opy_.POST:
                name = str(EVENTS.bstack11ll11111l_opy_.name)+bstack1ll1l_opy_ (u"ࠥ࠾ࠧሏ")+str(test_framework_state.name)
                bstack1l1lllll111_opy_ = TestFramework.bstack1l1lllll1ll_opy_(instance, name)
                bstack1llll1l1l11_opy_.end(EVENTS.bstack11ll11111l_opy_.value, bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦሐ"), bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥሑ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨሒ").format(e))
    def bstack1ll11lll1ll_opy_(self):
        return self.bstack1ll1l1lll1l_opy_
    def __1ll111l111l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1ll1l_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦሓ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll111lll1l_opy_(rep, [bstack1ll1l_opy_ (u"ࠣࡹ࡫ࡩࡳࠨሔ"), bstack1ll1l_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥሕ"), bstack1ll1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥሖ"), bstack1ll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦሗ"), bstack1ll1l_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠨመ"), bstack1ll1l_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧሙ")])
        return None
    def __1ll1l1111l1_opy_(self, instance: bstack1lll1l1l1ll_opy_, *args):
        result = self.__1ll111l111l_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l11l1_opy_ = None
        if result.get(bstack1ll1l_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣሚ"), None) == bstack1ll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣማ") and len(args) > 1 and getattr(args[1], bstack1ll1l_opy_ (u"ࠤࡨࡼࡨ࡯࡮ࡧࡱࠥሜ"), None) is not None:
            failure = [{bstack1ll1l_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ም"): [args[1].excinfo.exconly(), result.get(bstack1ll1l_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥሞ"), None)]}]
            bstack11111l11l1_opy_ = bstack1ll1l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨሟ") if bstack1ll1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤሠ") in getattr(args[1].excinfo, bstack1ll1l_opy_ (u"ࠢࡵࡻࡳࡩࡳࡧ࡭ࡦࠤሡ"), bstack1ll1l_opy_ (u"ࠣࠤሢ")) else bstack1ll1l_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥሣ")
        bstack1ll1l11ll1l_opy_ = result.get(bstack1ll1l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦሤ"), TestFramework.bstack1ll111ll1l1_opy_)
        if bstack1ll1l11ll1l_opy_ != TestFramework.bstack1ll111ll1l1_opy_:
            TestFramework.bstack1111111ll1_opy_(instance, TestFramework.bstack1l1llllll1l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l1l11ll_opy_(instance, {
            TestFramework.bstack1llll1111ll_opy_: failure,
            TestFramework.bstack1ll11llll11_opy_: bstack11111l11l1_opy_,
            TestFramework.bstack1lll1l11l1l_opy_: bstack1ll1l11ll1l_opy_,
        })
    def __1ll1l111lll_opy_(
        self,
        context: bstack1ll1l1lllll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1lll1llll11_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll11l1ll_opy_.SETUP_FIXTURE:
            instance = self.__1ll11111ll1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll111ll111_opy_ bstack1ll111l1111_opy_ this to be bstack1ll1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦሥ")
            if test_framework_state == bstack1llll11l1ll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1111lll1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1ll1l_opy_ (u"ࠧࡴ࡯ࡥࡧࠥሦ"), None), bstack1ll1l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨሧ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1ll1l_opy_ (u"ࠢ࡯ࡱࡧࡩࠧረ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1ll1l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣሩ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1l1lllllll1_opy_(target) if target else None
        return instance
    def __1ll11ll1l11_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1lll1llll11_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l1l111l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11ll1l1l_opy_, {})
        if not key in bstack1ll1l1l111l_opy_:
            bstack1ll1l1l111l_opy_[key] = []
        bstack1ll111lllll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11111lll_opy_, {})
        if not key in bstack1ll111lllll_opy_:
            bstack1ll111lllll_opy_[key] = []
        bstack1ll11l1ll1l_opy_ = {
            PytestBDDFramework.bstack1ll11ll1l1l_opy_: bstack1ll1l1l111l_opy_,
            PytestBDDFramework.bstack1ll11111lll_opy_: bstack1ll111lllll_opy_,
        }
        if test_hook_state == bstack1lll1llll11_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1ll1l_opy_ (u"ࠤ࡮ࡩࡾࠨሪ"): key,
                TestFramework.bstack1ll1l1ll1ll_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l111ll_opy_: TestFramework.bstack1ll1l11l1ll_opy_,
                TestFramework.bstack1ll1l111111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11ll111l_opy_: [],
                TestFramework.bstack1ll11l1l111_opy_: hook_name,
                TestFramework.bstack1ll11ll11l1_opy_: bstack1l1lllll1l1_opy_.bstack1ll11l1111l_opy_()
            }
            bstack1ll1l1l111l_opy_[key].append(hook)
            bstack1ll11l1ll1l_opy_[PytestBDDFramework.bstack1ll111l1lll_opy_] = key
        elif test_hook_state == bstack1lll1llll11_opy_.POST:
            bstack1ll11lll1l1_opy_ = bstack1ll1l1l111l_opy_.get(key, [])
            hook = bstack1ll11lll1l1_opy_.pop() if bstack1ll11lll1l1_opy_ else None
            if hook:
                result = self.__1ll111l111l_opy_(*args)
                if result:
                    bstack1ll1ll11l11_opy_ = result.get(bstack1ll1l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦራ"), TestFramework.bstack1ll1l11l1ll_opy_)
                    if bstack1ll1ll11l11_opy_ != TestFramework.bstack1ll1l11l1ll_opy_:
                        hook[TestFramework.bstack1ll11l111ll_opy_] = bstack1ll1ll11l11_opy_
                hook[TestFramework.bstack1ll11111l1l_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11ll11l1_opy_] = bstack1l1lllll1l1_opy_.bstack1ll11l1111l_opy_()
                self.bstack1ll11l1l1ll_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll111ll1ll_opy_, [])
                self.bstack1ll1l1ll111_opy_(instance, logs)
                bstack1ll111lllll_opy_[key].append(hook)
                bstack1ll11l1ll1l_opy_[PytestBDDFramework.bstack1ll1l1111ll_opy_] = key
        TestFramework.bstack1ll1l1l11ll_opy_(instance, bstack1ll11l1ll1l_opy_)
        self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢ࡬ࡴࡵ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡰ࡫ࡹࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࡃࡻࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࡽࠡࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠿ࠥሬ") + str(bstack1ll111lllll_opy_) + bstack1ll1l_opy_ (u"ࠧࠨር"))
    def __1ll11111ll1_opy_(
        self,
        context: bstack1ll1l1lllll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1lll1llll11_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll111lll1l_opy_(args[0], [bstack1ll1l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧሮ"), bstack1ll1l_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣሯ"), bstack1ll1l_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣሰ"), bstack1ll1l_opy_ (u"ࠤ࡬ࡨࡸࠨሱ"), bstack1ll1l_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧሲ"), bstack1ll1l_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦሳ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1ll1l_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦሴ")) else fixturedef.get(bstack1ll1l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧስ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1ll1l_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࠧሶ")) else None
        node = request.node if hasattr(request, bstack1ll1l_opy_ (u"ࠣࡰࡲࡨࡪࠨሷ")) else None
        target = request.node.nodeid if hasattr(node, bstack1ll1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤሸ")) else None
        baseid = fixturedef.get(bstack1ll1l_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥሹ"), None) or bstack1ll1l_opy_ (u"ࠦࠧሺ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1ll1l_opy_ (u"ࠧࡥࡰࡺࡨࡸࡲࡨ࡯ࡴࡦ࡯ࠥሻ")):
            target = PytestBDDFramework.__1ll1l1l1l1l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1ll1l_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣሼ")) else None
            if target and not TestFramework.bstack1l1lllllll1_opy_(target):
                self.__1ll1111lll1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡱࡳࡩ࡫࠽ࡼࡰࡲࡨࡪࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሽ") + str(test_hook_state) + bstack1ll1l_opy_ (u"ࠣࠤሾ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢሿ") + str(target) + bstack1ll1l_opy_ (u"ࠥࠦቀ"))
            return None
        instance = TestFramework.bstack1l1lllllll1_opy_(target)
        if not instance:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡦࡦࡹࡥࡪࡦࡀࡿࡧࡧࡳࡦ࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨቁ") + str(target) + bstack1ll1l_opy_ (u"ࠧࠨቂ"))
            return None
        bstack1ll11111111_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l1l11l1_opy_, {})
        if os.getenv(bstack1ll1l_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡌࡉ࡙ࡖࡘࡖࡊ࡙ࠢቃ"), bstack1ll1l_opy_ (u"ࠢ࠲ࠤቄ")) == bstack1ll1l_opy_ (u"ࠣ࠳ࠥቅ"):
            bstack1ll1l1l1ll1_opy_ = bstack1ll1l_opy_ (u"ࠤ࠽ࠦቆ").join((scope, fixturename))
            bstack1ll1111l1l1_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11l11ll1_opy_ = {
                bstack1ll1l_opy_ (u"ࠥ࡯ࡪࡿࠢቇ"): bstack1ll1l1l1ll1_opy_,
                bstack1ll1l_opy_ (u"ࠦࡹࡧࡧࡴࠤቈ"): PytestBDDFramework.__1ll111l1ll1_opy_(request.node, scenario),
                bstack1ll1l_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࠨ቉"): fixturedef,
                bstack1ll1l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧቊ"): scope,
                bstack1ll1l_opy_ (u"ࠢࡵࡻࡳࡩࠧቋ"): None,
            }
            try:
                if test_hook_state == bstack1lll1llll11_opy_.POST and callable(getattr(args[-1], bstack1ll1l_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧቌ"), None)):
                    bstack1ll11l11ll1_opy_[bstack1ll1l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢቍ")] = TestFramework.bstack1ll11l1ll11_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1llll11_opy_.PRE:
                bstack1ll11l11ll1_opy_[bstack1ll1l_opy_ (u"ࠥࡹࡺ࡯ࡤࠣ቎")] = uuid4().__str__()
                bstack1ll11l11ll1_opy_[PytestBDDFramework.bstack1ll1l111111_opy_] = bstack1ll1111l1l1_opy_
            elif test_hook_state == bstack1lll1llll11_opy_.POST:
                bstack1ll11l11ll1_opy_[PytestBDDFramework.bstack1ll11111l1l_opy_] = bstack1ll1111l1l1_opy_
            if bstack1ll1l1l1ll1_opy_ in bstack1ll11111111_opy_:
                bstack1ll11111111_opy_[bstack1ll1l1l1ll1_opy_].update(bstack1ll11l11ll1_opy_)
                self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࠧ቏") + str(bstack1ll11111111_opy_[bstack1ll1l1l1ll1_opy_]) + bstack1ll1l_opy_ (u"ࠧࠨቐ"))
            else:
                bstack1ll11111111_opy_[bstack1ll1l1l1ll1_opy_] = bstack1ll11l11ll1_opy_
                self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࢀࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࢁࠥࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࠤቑ") + str(len(bstack1ll11111111_opy_)) + bstack1ll1l_opy_ (u"ࠢࠣቒ"))
        TestFramework.bstack1111111ll1_opy_(instance, PytestBDDFramework.bstack1ll1l1l11l1_opy_, bstack1ll11111111_opy_)
        self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࡾࡰࡪࡴࠨࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠬࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣቓ") + str(instance.ref()) + bstack1ll1l_opy_ (u"ࠤࠥቔ"))
        return instance
    def __1ll1111lll1_opy_(
        self,
        context: bstack1ll1l1lllll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1lll111l_opy_.create_context(target)
        ob = bstack1lll1l1l1ll_opy_(ctx, self.bstack1ll1ll111ll_opy_, self.bstack1l1llllll11_opy_, test_framework_state)
        TestFramework.bstack1ll1l1l11ll_opy_(ob, {
            TestFramework.bstack1llll11llll_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l11l11_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l11l111_opy_: [],
            PytestBDDFramework.bstack1ll1l1l11l1_opy_: {},
            PytestBDDFramework.bstack1ll11111lll_opy_: {},
            PytestBDDFramework.bstack1ll11ll1l1l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1111111ll1_opy_(ob, TestFramework.bstack1ll11111l11_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1111111ll1_opy_(ob, TestFramework.bstack1lllllllll1_opy_, context.platform_index)
        TestFramework.bstack1lll1ll11ll_opy_[ctx.id] = ob
        self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡨࡺࡸ࠯࡫ࡧࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥቕ") + str(TestFramework.bstack1lll1ll11ll_opy_.keys()) + bstack1ll1l_opy_ (u"ࠦࠧቖ"))
        return ob
    @staticmethod
    def __1ll1l11llll_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1ll1l_opy_ (u"ࠬ࡯ࡤࠨ቗"): id(step),
                bstack1ll1l_opy_ (u"࠭ࡴࡦࡺࡷࠫቘ"): step.name,
                bstack1ll1l_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨ቙"): step.keyword,
            })
        meta = {
            bstack1ll1l_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩቚ"): {
                bstack1ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧቛ"): feature.name,
                bstack1ll1l_opy_ (u"ࠪࡴࡦࡺࡨࠨቜ"): feature.filename,
                bstack1ll1l_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩቝ"): feature.description
            },
            bstack1ll1l_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ቞"): {
                bstack1ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ቟"): scenario.name
            },
            bstack1ll1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭በ"): steps,
            bstack1ll1l_opy_ (u"ࠨࡧࡻࡥࡲࡶ࡬ࡦࡵࠪቡ"): PytestBDDFramework.__1ll111l1l11_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll111llll1_opy_: meta
            }
        )
    def bstack1ll11l1l1ll_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1ll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡳࡱࡦࡩࡸࡹࡥࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡴ࡫ࡰ࡭ࡱࡧࡲࠡࡶࡲࠤࡹ࡮ࡥࠡࡌࡤࡺࡦࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬࡮ࡹࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡃࡩࡧࡦ࡯ࡸࠦࡴࡩࡧࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡬ࡲࡸ࡯ࡤࡦࠢࢁ࠳࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠳࡚ࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡉࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡵࡩࡵࡲࡡࡤࡧࡶࠤ࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠦࠥ࡯࡮ࠡ࡫ࡷࡷࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡌࡪࠥࡧࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡯ࡤࡸࡨ࡮ࡥࡴࠢࡤࠤࡲࡵࡤࡪࡨ࡬ࡩࡩࠦࡨࡰࡱ࡮࠱ࡱ࡫ࡶࡦ࡮ࠣࡪ࡮ࡲࡥ࠭ࠢ࡬ࡸࠥࡩࡲࡦࡣࡷࡩࡸࠦࡡࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࠣࡻ࡮ࡺࡨࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡪࡥࡵࡣ࡬ࡰࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡙ࠥࡩ࡮࡫࡯ࡥࡷࡲࡹ࠭ࠢ࡬ࡸࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡰࡴࡩࡡࡵࡧࡧࠤ࡮ࡴࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡥࡽࠥࡸࡥࡱ࡮ࡤࡧ࡮ࡴࡧࠡࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭࠱ࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠣ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡖ࡫ࡩࠥࡩࡲࡦࡣࡷࡩࡩࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡤࡶࡪࠦࡡࡥࡦࡨࡨࠥࡺ࡯ࠡࡶ࡫ࡩࠥ࡮࡯ࡰ࡭ࠪࡷࠥࠨ࡬ࡰࡩࡶࠦࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࠺ࠡࡖ࡫ࡩࠥ࡫ࡶࡦࡰࡷࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷࠥࡧ࡮ࡥࠢ࡫ࡳࡴࡱࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬ࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡘࡪࡹࡴࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡹ࡮ࡲࡤࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡒࡤࡸ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣቢ")
        global _1ll11l11111_opy_
        platform_index = os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪባ")]
        bstack1ll1ll111l1_opy_ = os.path.join(bstack1ll1111llll_opy_, (bstack1ll1l11lll1_opy_ + str(platform_index)), bstack1ll11l1l1l1_opy_)
        if not os.path.exists(bstack1ll1ll111l1_opy_) or not os.path.isdir(bstack1ll1ll111l1_opy_):
            return
        logs = hook.get(bstack1ll1l_opy_ (u"ࠦࡱࡵࡧࡴࠤቤ"), [])
        with os.scandir(bstack1ll1ll111l1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11l11111_opy_:
                    self.logger.info(bstack1ll1l_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥብ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1ll1l_opy_ (u"ࠨࠢቦ")
                    log_entry = bstack1ll11lll111_opy_(
                        kind=bstack1ll1l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤቧ"),
                        message=bstack1ll1l_opy_ (u"ࠣࠤቨ"),
                        level=bstack1ll1l_opy_ (u"ࠤࠥቩ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11ll11ll_opy_=entry.stat().st_size,
                        bstack1l1llllllll_opy_=bstack1ll1l_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥቪ"),
                        bstack1ll1ll_opy_=os.path.abspath(entry.path),
                        bstack1ll11l11lll_opy_=hook.get(TestFramework.bstack1ll1l1ll1ll_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11l11111_opy_.add(abs_path)
        platform_index = os.environ[bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫቫ")]
        bstack1ll111l11l1_opy_ = os.path.join(bstack1ll1111llll_opy_, (bstack1ll1l11lll1_opy_ + str(platform_index)), bstack1ll11l1l1l1_opy_, bstack1ll1111l1ll_opy_)
        if not os.path.exists(bstack1ll111l11l1_opy_) or not os.path.isdir(bstack1ll111l11l1_opy_):
            self.logger.info(bstack1ll1l_opy_ (u"ࠧࡔ࡯ࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࡨࡲࡹࡳࡪࠠࡢࡶ࠽ࠤࢀࢃࠢቬ").format(bstack1ll111l11l1_opy_))
        else:
            self.logger.info(bstack1ll1l_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡧࡴࡲࡱࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠻ࠢࡾࢁࠧቭ").format(bstack1ll111l11l1_opy_))
            with os.scandir(bstack1ll111l11l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11l11111_opy_:
                        self.logger.info(bstack1ll1l_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧቮ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1ll1l_opy_ (u"ࠣࠤቯ")
                        log_entry = bstack1ll11lll111_opy_(
                            kind=bstack1ll1l_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦተ"),
                            message=bstack1ll1l_opy_ (u"ࠥࠦቱ"),
                            level=bstack1ll1l_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣቲ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11ll11ll_opy_=entry.stat().st_size,
                            bstack1l1llllllll_opy_=bstack1ll1l_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧታ"),
                            bstack1ll1ll_opy_=os.path.abspath(entry.path),
                            bstack1ll11llll1l_opy_=hook.get(TestFramework.bstack1ll1l1ll1ll_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11l11111_opy_.add(abs_path)
        hook[bstack1ll1l_opy_ (u"ࠨ࡬ࡰࡩࡶࠦቴ")] = logs
    def bstack1ll1l1ll111_opy_(
        self,
        bstack1ll1111111l_opy_: bstack1lll1l1l1ll_opy_,
        entries: List[bstack1ll11lll111_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡔࡇࡖࡗࡎࡕࡎࡠࡋࡇࠦት"))
        req.platform_index = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1lllllllll1_opy_)
        req.execution_context.hash = str(bstack1ll1111111l_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1111111l_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1111111l_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1llll11llll_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1lll1l11l11_opy_)
            log_entry.uuid = entry.bstack1ll11l11lll_opy_ if entry.bstack1ll11l11lll_opy_ else TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1llll11ll1l_opy_)
            log_entry.test_framework_state = bstack1ll1111111l_opy_.state.name
            log_entry.message = entry.message.encode(bstack1ll1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢቶ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1ll1l_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦቷ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11ll11ll_opy_
                log_entry.file_path = entry.bstack1ll1ll_opy_
        def bstack1ll1l1ll1l1_opy_():
            bstack1l11l11lll_opy_ = datetime.now()
            try:
                self.bstack1llll1l1ll1_opy_.LogCreatedEvent(req)
                bstack1ll1111111l_opy_.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠢቸ"), datetime.now() - bstack1l11l11lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1ll1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡼࡿࠥቹ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll1l1ll1l1_opy_)
    def __1ll11ll1ll1_opy_(self, instance) -> None:
        bstack1ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡏࡳࡦࡪࡳࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࡸࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡸࡥࡢࡶࡨࡷࠥࡧࠠࡥ࡫ࡦࡸࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡭ࡧࡹࡩࡱࠦࡣࡶࡵࡷࡳࡲࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡺࡹࡴࡰ࡯ࡗࡥ࡬ࡓࡡ࡯ࡣࡪࡩࡷࠦࡡ࡯ࡦࠣࡹࡵࡪࡡࡵࡧࡶࠤࡹ࡮ࡥࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡷࡹࡧࡴࡦࠢࡸࡷ࡮ࡴࡧࠡࡵࡨࡸࡤࡹࡴࡢࡶࡨࡣࡪࡴࡴࡳ࡫ࡨࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥቺ")
        bstack1ll11l1ll1l_opy_ = {bstack1ll1l_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠣቻ"): bstack1l1lllll1l1_opy_.bstack1ll11l1111l_opy_()}
        TestFramework.bstack1ll1l1l11ll_opy_(instance, bstack1ll11l1ll1l_opy_)
    @staticmethod
    def __1ll11lll11l_opy_(instance, args):
        request, bstack1ll1l1llll1_opy_ = args
        bstack1ll111111l1_opy_ = id(bstack1ll1l1llll1_opy_)
        bstack1ll11lllll1_opy_ = instance.data[TestFramework.bstack1ll111llll1_opy_]
        step = next(filter(lambda st: st[bstack1ll1l_opy_ (u"ࠧࡪࡦࠪቼ")] == bstack1ll111111l1_opy_, bstack1ll11lllll1_opy_[bstack1ll1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧች")]), None)
        step.update({
            bstack1ll1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ቾ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll11lllll1_opy_[bstack1ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩቿ")]) if st[bstack1ll1l_opy_ (u"ࠫ࡮ࡪࠧኀ")] == step[bstack1ll1l_opy_ (u"ࠬ࡯ࡤࠨኁ")]), None)
        if index is not None:
            bstack1ll11lllll1_opy_[bstack1ll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኂ")][index] = step
        instance.data[TestFramework.bstack1ll111llll1_opy_] = bstack1ll11lllll1_opy_
    @staticmethod
    def __1ll11ll1111_opy_(instance, args):
        bstack1ll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡼ࡮ࡥ࡯ࠢ࡯ࡩࡳࠦࡡࡳࡩࡶࠤ࡮ࡹࠠ࠳࠮ࠣ࡭ࡹࠦࡳࡪࡩࡱ࡭࡫࡯ࡥࡴࠢࡷ࡬ࡪࡸࡥࠡ࡫ࡶࠤࡳࡵࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡵ࡫ࡸࠦࡡࡳࡧࠣ࠱ࠥࡡࡲࡦࡳࡸࡩࡸࡺࠬࠡࡵࡷࡩࡵࡣࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠳ࠡࡶ࡫ࡩࡳࠦࡴࡩࡧࠣࡰࡦࡹࡴࠡࡸࡤࡰࡺ࡫ࠠࡪࡵࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥኃ")
        bstack1ll1l1l1lll_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll1l1llll1_opy_ = args[1]
        bstack1ll111111l1_opy_ = id(bstack1ll1l1llll1_opy_)
        bstack1ll11lllll1_opy_ = instance.data[TestFramework.bstack1ll111llll1_opy_]
        step = None
        if bstack1ll111111l1_opy_ is not None and bstack1ll11lllll1_opy_.get(bstack1ll1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኄ")):
            step = next(filter(lambda st: st[bstack1ll1l_opy_ (u"ࠩ࡬ࡨࠬኅ")] == bstack1ll111111l1_opy_, bstack1ll11lllll1_opy_[bstack1ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኆ")]), None)
            step.update({
                bstack1ll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩኇ"): bstack1ll1l1l1lll_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1ll1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬኈ"): bstack1ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭኉"),
                bstack1ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨኊ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1ll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨኋ"): bstack1ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩኌ"),
                })
        index = next((i for i, st in enumerate(bstack1ll11lllll1_opy_[bstack1ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኍ")]) if st[bstack1ll1l_opy_ (u"ࠫ࡮ࡪࠧ኎")] == step[bstack1ll1l_opy_ (u"ࠬ࡯ࡤࠨ኏")]), None)
        if index is not None:
            bstack1ll11lllll1_opy_[bstack1ll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬነ")][index] = step
        instance.data[TestFramework.bstack1ll111llll1_opy_] = bstack1ll11lllll1_opy_
    @staticmethod
    def __1ll111l1l11_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1ll1l_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩኑ")):
                examples = list(node.callspec.params[bstack1ll1l_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧኒ")].values())
            return examples
        except:
            return []
    def bstack1ll1l111l1l_opy_(self, instance: bstack1lll1l1l1ll_opy_, bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_]):
        bstack1ll111lll11_opy_ = (
            PytestBDDFramework.bstack1ll111l1lll_opy_
            if bstack1llllll111l_opy_[1] == bstack1lll1llll11_opy_.PRE
            else PytestBDDFramework.bstack1ll1l1111ll_opy_
        )
        hook = PytestBDDFramework.bstack1ll111ll11l_opy_(instance, bstack1ll111lll11_opy_)
        entries = hook.get(TestFramework.bstack1ll11ll111l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l11l111_opy_, []))
        return entries
    def bstack1ll11l1lll1_opy_(self, instance: bstack1lll1l1l1ll_opy_, bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_]):
        bstack1ll111lll11_opy_ = (
            PytestBDDFramework.bstack1ll111l1lll_opy_
            if bstack1llllll111l_opy_[1] == bstack1lll1llll11_opy_.PRE
            else PytestBDDFramework.bstack1ll1l1111ll_opy_
        )
        PytestBDDFramework.bstack1ll1111l111_opy_(instance, bstack1ll111lll11_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l11l111_opy_, []).clear()
    @staticmethod
    def bstack1ll111ll11l_opy_(instance: bstack1lll1l1l1ll_opy_, bstack1ll111lll11_opy_: str):
        bstack1ll1l1ll11l_opy_ = (
            PytestBDDFramework.bstack1ll11111lll_opy_
            if bstack1ll111lll11_opy_ == PytestBDDFramework.bstack1ll1l1111ll_opy_
            else PytestBDDFramework.bstack1ll11ll1l1l_opy_
        )
        bstack1ll11l11l1l_opy_ = TestFramework.get_state(instance, bstack1ll111lll11_opy_, None)
        bstack1ll111111ll_opy_ = TestFramework.get_state(instance, bstack1ll1l1ll11l_opy_, None) if bstack1ll11l11l1l_opy_ else None
        return (
            bstack1ll111111ll_opy_[bstack1ll11l11l1l_opy_][-1]
            if isinstance(bstack1ll111111ll_opy_, dict) and len(bstack1ll111111ll_opy_.get(bstack1ll11l11l1l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1111l111_opy_(instance: bstack1lll1l1l1ll_opy_, bstack1ll111lll11_opy_: str):
        hook = PytestBDDFramework.bstack1ll111ll11l_opy_(instance, bstack1ll111lll11_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11ll111l_opy_, []).clear()
    @staticmethod
    def __1l1llll1ll1_opy_(instance: bstack1lll1l1l1ll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1ll1l_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡥࡲࡶࡩࡹࠢና"), None)):
            return
        if os.getenv(bstack1ll1l_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡏࡓࡌ࡙ࠢኔ"), bstack1ll1l_opy_ (u"ࠦ࠶ࠨን")) != bstack1ll1l_opy_ (u"ࠧ࠷ࠢኖ"):
            PytestBDDFramework.logger.warning(bstack1ll1l_opy_ (u"ࠨࡩࡨࡰࡲࡶ࡮ࡴࡧࠡࡥࡤࡴࡱࡵࡧࠣኗ"))
            return
        bstack1ll1111ll11_opy_ = {
            bstack1ll1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨኘ"): (PytestBDDFramework.bstack1ll111l1lll_opy_, PytestBDDFramework.bstack1ll11ll1l1l_opy_),
            bstack1ll1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥኙ"): (PytestBDDFramework.bstack1ll1l1111ll_opy_, PytestBDDFramework.bstack1ll11111lll_opy_),
        }
        for when in (bstack1ll1l_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣኚ"), bstack1ll1l_opy_ (u"ࠥࡧࡦࡲ࡬ࠣኛ"), bstack1ll1l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨኜ")):
            bstack1ll1l11111l_opy_ = args[1].get_records(when)
            if not bstack1ll1l11111l_opy_:
                continue
            records = [
                bstack1ll11lll111_opy_(
                    kind=TestFramework.bstack1ll11l1l11l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1ll1l_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠣኝ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1ll1l_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪࠢኞ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1l11111l_opy_
                if isinstance(getattr(r, bstack1ll1l_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣኟ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll1l111ll1_opy_, bstack1ll1l1ll11l_opy_ = bstack1ll1111ll11_opy_.get(when, (None, None))
            bstack1ll1l111l11_opy_ = TestFramework.get_state(instance, bstack1ll1l111ll1_opy_, None) if bstack1ll1l111ll1_opy_ else None
            bstack1ll111111ll_opy_ = TestFramework.get_state(instance, bstack1ll1l1ll11l_opy_, None) if bstack1ll1l111l11_opy_ else None
            if isinstance(bstack1ll111111ll_opy_, dict) and len(bstack1ll111111ll_opy_.get(bstack1ll1l111l11_opy_, [])) > 0:
                hook = bstack1ll111111ll_opy_[bstack1ll1l111l11_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11ll111l_opy_ in hook:
                    hook[TestFramework.bstack1ll11ll111l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l11l111_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l1l1111_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1l11l1l1_opy_(request.node, scenario)
        bstack1l1lllll11l_opy_ = feature.filename
        if not test_id or not test_name or not bstack1l1lllll11l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1llll11ll1l_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11l1llll_opy_: test_id,
            TestFramework.bstack1ll1l11l11l_opy_: test_name,
            TestFramework.bstack1ll111l11ll_opy_: test_id,
            TestFramework.bstack1ll1ll11111_opy_: bstack1l1lllll11l_opy_,
            TestFramework.bstack1ll1l1lll11_opy_: PytestBDDFramework.__1ll111l1ll1_opy_(feature, scenario),
            TestFramework.bstack1ll11l111l1_opy_: code,
            TestFramework.bstack1lll1l11l1l_opy_: TestFramework.bstack1ll111ll1l1_opy_,
            TestFramework.bstack1lll111llll_opy_: test_name
        }
    @staticmethod
    def __1ll1l11l1l1_opy_(node, scenario):
        if hasattr(node, bstack1ll1l_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪአ")):
            parts = node.nodeid.rsplit(bstack1ll1l_opy_ (u"ࠤ࡞ࠦኡ"))
            params = parts[-1]
            return bstack1ll1l_opy_ (u"ࠥࡿࢂ࡛ࠦࡼࡿࠥኢ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll111l1ll1_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1ll1l_opy_ (u"ࠫࡹࡧࡧࡴࠩኣ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1ll1l_opy_ (u"ࠬࡺࡡࡨࡵࠪኤ")) else [])
    @staticmethod
    def __1ll1l1l1l1l_opy_(location):
        return bstack1ll1l_opy_ (u"ࠨ࠺࠻ࠤእ").join(filter(lambda x: isinstance(x, str), location))