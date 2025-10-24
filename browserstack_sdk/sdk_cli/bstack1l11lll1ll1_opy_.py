# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1ll11ll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack111llll11l_opy_ import bstack1ll11l1l1ll_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll11l11l_opy_,
    bstack1lll1l11111_opy_,
    bstack1lll11llll1_opy_,
    bstack1ll1l1l11l1_opy_,
    bstack1ll111ll111_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1l1llll1111_opy_
from bstack_utils.bstack111l11l11_opy_ import bstack1lllllll11l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11l1ll1_opy_ import bstack1lll11ll111_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll111ll11l_opy_ import bstack1ll11llllll_opy_
from bstack_utils.bstack1l1l1l1l_opy_ import bstack1l111ll1_opy_
bstack1ll11lll11l_opy_ = bstack1l1llll1111_opy_()
bstack1ll1l11l111_opy_ = 1.0
bstack1ll1111llll_opy_ = bstack1l1_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣᕿ")
bstack11llll11l1l_opy_ = bstack1l1_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᖀ")
bstack11llll11l11_opy_ = bstack1l1_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᖁ")
bstack11llll111ll_opy_ = bstack1l1_opy_ (u"ࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢᖂ")
bstack11llll11ll1_opy_ = bstack1l1_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦᖃ")
_1l1llll1lll_opy_ = set()
class bstack1l11ll11lll_opy_(TestFramework):
    bstack1ll11ll1l11_opy_ = bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᖄ")
    bstack1ll11l111ll_opy_ = bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࠧᖅ")
    bstack1ll1l111l1l_opy_ = bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᖆ")
    bstack1ll1l111ll1_opy_ = bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࠦᖇ")
    bstack1ll1l1l1ll1_opy_ = bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨᖈ")
    bstack1ll1l1ll1ll_opy_: bool
    bstack1lll11l1ll1_opy_: bstack1lll11ll111_opy_  = None
    bstack1llll1l11ll_opy_ = None
    bstack1ll11lll1ll_opy_ = [
        bstack1llll11l11l_opy_.BEFORE_ALL,
        bstack1llll11l11l_opy_.AFTER_ALL,
        bstack1llll11l11l_opy_.BEFORE_EACH,
        bstack1llll11l11l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11lllll1_opy_: Dict[str, str],
        bstack1ll11111ll1_opy_: List[str]=[bstack1l1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᖉ")],
        bstack1lll11l1ll1_opy_: bstack1lll11ll111_opy_=None,
        bstack1llll1l11ll_opy_=None
    ):
        super().__init__(bstack1ll11111ll1_opy_, bstack1ll11lllll1_opy_, bstack1lll11l1ll1_opy_)
        self.bstack1ll1l1ll1ll_opy_ = any(bstack1l1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᖊ") in item.lower() for item in bstack1ll11111ll1_opy_)
        self.bstack1llll1l11ll_opy_ = bstack1llll1l11ll_opy_
    def track_event(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        test_hook_state: bstack1lll11llll1_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll11l11l_opy_.TEST or test_framework_state in bstack1l11ll11lll_opy_.bstack1ll11lll1ll_opy_:
            bstack1ll11l1l1ll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll11l11l_opy_.NONE:
            self.logger.warning(bstack1l1_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࠢᖋ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠢࠣᖌ"))
            return
        if not self.bstack1ll1l1ll1ll_opy_:
            self.logger.warning(bstack1l1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠾ࠤᖍ") + str(str(self.bstack1ll11111ll1_opy_)) + bstack1l1_opy_ (u"ࠤࠥᖎ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᖏ") + str(kwargs) + bstack1l1_opy_ (u"ࠦࠧᖐ"))
            return
        instance = self.__1ll111lll1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࠦᖑ") + str(args) + bstack1l1_opy_ (u"ࠨࠢᖒ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l11ll11lll_opy_.bstack1ll11lll1ll_opy_ and test_hook_state == bstack1lll11llll1_opy_.PRE:
                bstack1ll11ll1lll_opy_ = bstack1lllllll11l_opy_.bstack1ll1l1l1lll_opy_(EVENTS.bstack1l1l1l11l_opy_.value)
                name = str(EVENTS.bstack1l1l1l11l_opy_.name)+bstack1l1_opy_ (u"ࠢ࠻ࠤᖓ")+str(test_framework_state.name)
                TestFramework.bstack1ll11111l1l_opy_(instance, name, bstack1ll11ll1lll_opy_)
        except Exception as e:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵࠤࡵࡸࡥ࠻ࠢࡾࢁࠧᖔ").format(e))
        try:
            if not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l1111l1_opy_) and test_hook_state == bstack1lll11llll1_opy_.PRE:
                test = bstack1l11ll11lll_opy_.__1ll11llll1l_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1l1_opy_ (u"ࠤ࡯ࡳࡦࡪࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖕ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠥࠦᖖ"))
            if test_framework_state == bstack1llll11l11l_opy_.TEST:
                if test_hook_state == bstack1lll11llll1_opy_.PRE and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll11l1ll1l_opy_):
                    TestFramework.bstack1llll1l1lll_opy_(instance, TestFramework.bstack1ll11l1ll1l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡳࡵࡣࡵࡸࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖗ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠧࠨᖘ"))
                elif test_hook_state == bstack1lll11llll1_opy_.POST and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1l1lllllll1_opy_):
                    TestFramework.bstack1llll1l1lll_opy_(instance, TestFramework.bstack1l1lllllll1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡧࡱࡨࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖙ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠢࠣᖚ"))
            elif test_framework_state == bstack1llll11l11l_opy_.LOG and test_hook_state == bstack1lll11llll1_opy_.POST:
                bstack1l11ll11lll_opy_.__1ll1l111111_opy_(instance, *args)
            elif test_framework_state == bstack1llll11l11l_opy_.LOG_REPORT and test_hook_state == bstack1lll11llll1_opy_.POST:
                self.__1ll111l1l11_opy_(instance, *args)
                self.__1ll11ll11ll_opy_(instance)
            elif test_framework_state in bstack1l11ll11lll_opy_.bstack1ll11lll1ll_opy_:
                self.__1ll1l11ll1l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᖛ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠤࠥᖜ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11l1lll1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l11ll11lll_opy_.bstack1ll11lll1ll_opy_ and test_hook_state == bstack1lll11llll1_opy_.POST:
                name = str(EVENTS.bstack1l1l1l11l_opy_.name)+bstack1l1_opy_ (u"ࠥ࠾ࠧᖝ")+str(test_framework_state.name)
                bstack1ll11ll1lll_opy_ = TestFramework.bstack1ll111ll1l1_opy_(instance, name)
                bstack1lllllll11l_opy_.end(EVENTS.bstack1l1l1l11l_opy_.value, bstack1ll11ll1lll_opy_+bstack1l1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᖞ"), bstack1ll11ll1lll_opy_+bstack1l1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᖟ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᖠ").format(e))
    def bstack1l1lllll1l1_opy_(self):
        return self.bstack1ll1l1ll1ll_opy_
    def __1ll1111ll11_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦᖡ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l1l111l_opy_(rep, [bstack1l1_opy_ (u"ࠣࡹ࡫ࡩࡳࠨᖢ"), bstack1l1_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᖣ"), bstack1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥᖤ"), bstack1l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᖥ"), bstack1l1_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠨᖦ"), bstack1l1_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧᖧ")])
        return None
    def __1ll111l1l11_opy_(self, instance: bstack1lll1l11111_opy_, *args):
        result = self.__1ll1111ll11_opy_(*args)
        if not result:
            return
        failure = None
        bstack111111l111_opy_ = None
        if result.get(bstack1l1_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᖨ"), None) == bstack1l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᖩ") and len(args) > 1 and getattr(args[1], bstack1l1_opy_ (u"ࠤࡨࡼࡨ࡯࡮ࡧࡱࠥᖪ"), None) is not None:
            failure = [{bstack1l1_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᖫ"): [args[1].excinfo.exconly(), result.get(bstack1l1_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥᖬ"), None)]}]
            bstack111111l111_opy_ = bstack1l1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᖭ") if bstack1l1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᖮ") in getattr(args[1].excinfo, bstack1l1_opy_ (u"ࠢࡵࡻࡳࡩࡳࡧ࡭ࡦࠤᖯ"), bstack1l1_opy_ (u"ࠣࠤᖰ")) else bstack1l1_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᖱ")
        bstack1ll111111ll_opy_ = result.get(bstack1l1_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᖲ"), TestFramework.bstack1ll11l1ll11_opy_)
        if bstack1ll111111ll_opy_ != TestFramework.bstack1ll11l1ll11_opy_:
            TestFramework.bstack1llll1l1lll_opy_(instance, TestFramework.bstack1l1lllll11l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l11llll_opy_(instance, {
            TestFramework.bstack1lll1ll11l1_opy_: failure,
            TestFramework.bstack1ll11ll1111_opy_: bstack111111l111_opy_,
            TestFramework.bstack1lll1ll11ll_opy_: bstack1ll111111ll_opy_,
        })
    def __1ll111lll1l_opy_(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        test_hook_state: bstack1lll11llll1_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll11l11l_opy_.SETUP_FIXTURE:
            instance = self.__1ll11111l11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1l1ll11l_opy_ bstack1ll11l1l11l_opy_ this to be bstack1l1_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᖳ")
            if test_framework_state == bstack1llll11l11l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll11llll11_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll11l11l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᖴ"), None), bstack1l1_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᖵ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᖶ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll1l11l1l1_opy_(target) if target else None
        return instance
    def __1ll1l11ll1l_opy_(
        self,
        instance: bstack1lll1l11111_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        test_hook_state: bstack1lll11llll1_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l1llllllll_opy_ = TestFramework.get_state(instance, bstack1l11ll11lll_opy_.bstack1ll11l111ll_opy_, {})
        if not key in bstack1l1llllllll_opy_:
            bstack1l1llllllll_opy_[key] = []
        bstack1ll1111l1l1_opy_ = TestFramework.get_state(instance, bstack1l11ll11lll_opy_.bstack1ll1l111l1l_opy_, {})
        if not key in bstack1ll1111l1l1_opy_:
            bstack1ll1111l1l1_opy_[key] = []
        bstack1ll111l111l_opy_ = {
            bstack1l11ll11lll_opy_.bstack1ll11l111ll_opy_: bstack1l1llllllll_opy_,
            bstack1l11ll11lll_opy_.bstack1ll1l111l1l_opy_: bstack1ll1111l1l1_opy_,
        }
        if test_hook_state == bstack1lll11llll1_opy_.PRE:
            hook = {
                bstack1l1_opy_ (u"ࠣ࡭ࡨࡽࠧᖷ"): key,
                TestFramework.bstack1ll1l111l11_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l1l111_opy_: TestFramework.bstack1ll1l11l1ll_opy_,
                TestFramework.bstack1ll1l11lll1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1111l1ll_opy_: [],
                TestFramework.bstack1l1llll11l1_opy_: args[1] if len(args) > 1 else bstack1l1_opy_ (u"ࠩࠪᖸ"),
                TestFramework.bstack1l1llllll1l_opy_: bstack1ll11llllll_opy_.bstack1l1llll1l11_opy_()
            }
            bstack1l1llllllll_opy_[key].append(hook)
            bstack1ll111l111l_opy_[bstack1l11ll11lll_opy_.bstack1ll1l111ll1_opy_] = key
        elif test_hook_state == bstack1lll11llll1_opy_.POST:
            bstack1ll111l11l1_opy_ = bstack1l1llllllll_opy_.get(key, [])
            hook = bstack1ll111l11l1_opy_.pop() if bstack1ll111l11l1_opy_ else None
            if hook:
                result = self.__1ll1111ll11_opy_(*args)
                if result:
                    bstack1ll11ll1l1l_opy_ = result.get(bstack1l1_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᖹ"), TestFramework.bstack1ll1l11l1ll_opy_)
                    if bstack1ll11ll1l1l_opy_ != TestFramework.bstack1ll1l11l1ll_opy_:
                        hook[TestFramework.bstack1ll11l1l111_opy_] = bstack1ll11ll1l1l_opy_
                hook[TestFramework.bstack1l1llllll11_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1l1llllll1l_opy_]= bstack1ll11llllll_opy_.bstack1l1llll1l11_opy_()
                self.bstack1ll1111l111_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11l111l1_opy_, [])
                if logs: self.bstack1ll1111ll1l_opy_(instance, logs)
                bstack1ll1111l1l1_opy_[key].append(hook)
                bstack1ll111l111l_opy_[bstack1l11ll11lll_opy_.bstack1ll1l1l1ll1_opy_] = key
        TestFramework.bstack1ll1l11llll_opy_(instance, bstack1ll111l111l_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢ࡬ࡴࡵ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡰ࡫ࡹࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࡃࡻࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࡽࠡࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠿ࠥᖺ") + str(bstack1ll1111l1l1_opy_) + bstack1l1_opy_ (u"ࠧࠨᖻ"))
    def __1ll11111l11_opy_(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        test_hook_state: bstack1lll11llll1_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l1l111l_opy_(args[0], [bstack1l1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᖼ"), bstack1l1_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣᖽ"), bstack1l1_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣᖾ"), bstack1l1_opy_ (u"ࠤ࡬ࡨࡸࠨᖿ"), bstack1l1_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧᗀ"), bstack1l1_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦᗁ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1l1_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᗂ")) else fixturedef.get(bstack1l1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᗃ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࠧᗄ")) else None
        node = request.node if hasattr(request, bstack1l1_opy_ (u"ࠣࡰࡲࡨࡪࠨᗅ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᗆ")) else None
        baseid = fixturedef.get(bstack1l1_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥᗇ"), None) or bstack1l1_opy_ (u"ࠦࠧᗈ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1_opy_ (u"ࠧࡥࡰࡺࡨࡸࡲࡨ࡯ࡴࡦ࡯ࠥᗉ")):
            target = bstack1l11ll11lll_opy_.__1ll1l11l11l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᗊ")) else None
            if target and not TestFramework.bstack1ll1l11l1l1_opy_(target):
                self.__1ll11llll11_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡱࡳࡩ࡫࠽ࡼࡰࡲࡨࡪࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᗋ") + str(test_hook_state) + bstack1l1_opy_ (u"ࠣࠤᗌ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢᗍ") + str(target) + bstack1l1_opy_ (u"ࠥࠦᗎ"))
            return None
        instance = TestFramework.bstack1ll1l11l1l1_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡦࡦࡹࡥࡪࡦࡀࡿࡧࡧࡳࡦ࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨᗏ") + str(target) + bstack1l1_opy_ (u"ࠧࠨᗐ"))
            return None
        bstack1ll11l11l1l_opy_ = TestFramework.get_state(instance, bstack1l11ll11lll_opy_.bstack1ll11ll1l11_opy_, {})
        if os.getenv(bstack1l1_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡌࡉ࡙ࡖࡘࡖࡊ࡙ࠢᗑ"), bstack1l1_opy_ (u"ࠢ࠲ࠤᗒ")) == bstack1l1_opy_ (u"ࠣ࠳ࠥᗓ"):
            bstack1ll1l1111ll_opy_ = bstack1l1_opy_ (u"ࠤ࠽ࠦᗔ").join((scope, fixturename))
            bstack1ll111l1lll_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll111llll1_opy_ = {
                bstack1l1_opy_ (u"ࠥ࡯ࡪࡿࠢᗕ"): bstack1ll1l1111ll_opy_,
                bstack1l1_opy_ (u"ࠦࡹࡧࡧࡴࠤᗖ"): bstack1l11ll11lll_opy_.__1ll11ll11l1_opy_(request.node),
                bstack1l1_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࠨᗗ"): fixturedef,
                bstack1l1_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᗘ"): scope,
                bstack1l1_opy_ (u"ࠢࡵࡻࡳࡩࠧᗙ"): None,
            }
            try:
                if test_hook_state == bstack1lll11llll1_opy_.POST and callable(getattr(args[-1], bstack1l1_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧᗚ"), None)):
                    bstack1ll111llll1_opy_[bstack1l1_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᗛ")] = TestFramework.bstack1ll1l1l11ll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll11llll1_opy_.PRE:
                bstack1ll111llll1_opy_[bstack1l1_opy_ (u"ࠥࡹࡺ࡯ࡤࠣᗜ")] = uuid4().__str__()
                bstack1ll111llll1_opy_[bstack1l11ll11lll_opy_.bstack1ll1l11lll1_opy_] = bstack1ll111l1lll_opy_
            elif test_hook_state == bstack1lll11llll1_opy_.POST:
                bstack1ll111llll1_opy_[bstack1l11ll11lll_opy_.bstack1l1llllll11_opy_] = bstack1ll111l1lll_opy_
            if bstack1ll1l1111ll_opy_ in bstack1ll11l11l1l_opy_:
                bstack1ll11l11l1l_opy_[bstack1ll1l1111ll_opy_].update(bstack1ll111llll1_opy_)
                self.logger.debug(bstack1l1_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࠧᗝ") + str(bstack1ll11l11l1l_opy_[bstack1ll1l1111ll_opy_]) + bstack1l1_opy_ (u"ࠧࠨᗞ"))
            else:
                bstack1ll11l11l1l_opy_[bstack1ll1l1111ll_opy_] = bstack1ll111llll1_opy_
                self.logger.debug(bstack1l1_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࢀࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࢁࠥࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࠤᗟ") + str(len(bstack1ll11l11l1l_opy_)) + bstack1l1_opy_ (u"ࠢࠣᗠ"))
        TestFramework.bstack1llll1l1lll_opy_(instance, bstack1l11ll11lll_opy_.bstack1ll11ll1l11_opy_, bstack1ll11l11l1l_opy_)
        self.logger.debug(bstack1l1_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࡾࡰࡪࡴࠨࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠬࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᗡ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠤࠥᗢ"))
        return instance
    def __1ll11llll11_opy_(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1llll11l11l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        ob = bstack1lll1l11111_opy_(ctx, self.bstack1ll11111ll1_opy_, self.bstack1ll11lllll1_opy_, test_framework_state)
        TestFramework.bstack1ll1l11llll_opy_(ob, {
            TestFramework.bstack1lll1l1111l_opy_: context.test_framework_name,
            TestFramework.bstack1lll1ll1l11_opy_: context.test_framework_version,
            TestFramework.bstack1l1lll1llll_opy_: [],
            bstack1l11ll11lll_opy_.bstack1ll11ll1l11_opy_: {},
            bstack1l11ll11lll_opy_.bstack1ll1l111l1l_opy_: {},
            bstack1l11ll11lll_opy_.bstack1ll11l111ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1l1lll_opy_(ob, TestFramework.bstack1ll111111l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1l1lll_opy_(ob, TestFramework.bstack1lllll1l11l_opy_, context.platform_index)
        TestFramework.bstack1lll1lllll1_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡨࡺࡸ࠯࡫ࡧࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥᗣ") + str(TestFramework.bstack1lll1lllll1_opy_.keys()) + bstack1l1_opy_ (u"ࠦࠧᗤ"))
        return ob
    def bstack1l1lll1lll1_opy_(self, instance: bstack1lll1l11111_opy_, bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_]):
        bstack1ll11ll111l_opy_ = (
            bstack1l11ll11lll_opy_.bstack1ll1l111ll1_opy_
            if bstack1lllll1l1l1_opy_[1] == bstack1lll11llll1_opy_.PRE
            else bstack1l11ll11lll_opy_.bstack1ll1l1l1ll1_opy_
        )
        hook = bstack1l11ll11lll_opy_.bstack1ll111lll11_opy_(instance, bstack1ll11ll111l_opy_)
        entries = hook.get(TestFramework.bstack1ll1111l1ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1l1lll1llll_opy_, []))
        return entries
    def bstack1ll1l1l1l11_opy_(self, instance: bstack1lll1l11111_opy_, bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_]):
        bstack1ll11ll111l_opy_ = (
            bstack1l11ll11lll_opy_.bstack1ll1l111ll1_opy_
            if bstack1lllll1l1l1_opy_[1] == bstack1lll11llll1_opy_.PRE
            else bstack1l11ll11lll_opy_.bstack1ll1l1l1ll1_opy_
        )
        bstack1l11ll11lll_opy_.bstack1ll1l111lll_opy_(instance, bstack1ll11ll111l_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1l1lll1llll_opy_, []).clear()
    def bstack1ll1111l111_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1l1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡷ࡮ࡳࡩ࡭ࡣࡵࠤࡹࡵࠠࡵࡪࡨࠤࡏࡧࡶࡢࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡪࡵࠣࡱࡪࡺࡨࡰࡦ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡆ࡬ࡪࡩ࡫ࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡯࡮ࡴ࡫ࡧࡩࠥࢄ࠯࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠯ࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠰ࠥࡸࡥࡱ࡮ࡤࡧࡪࡹࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢࠡ࡫ࡱࠤ࡮ࡺࡳࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡏࡦࠡࡣࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡲࡧࡴࡤࡪࡨࡷࠥࡧࠠ࡮ࡱࡧ࡭࡫࡯ࡥࡥࠢ࡫ࡳࡴࡱ࠭࡭ࡧࡹࡩࡱࠦࡦࡪ࡮ࡨ࠰ࠥ࡯ࡴࠡࡥࡵࡩࡦࡺࡥࡴࠢࡤࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡕ࡬ࡱ࡮ࡲࡡࡳ࡮ࡼ࠰ࠥ࡯ࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦ࡬ࡰࡥࡤࡸࡪࡪࠠࡪࡰࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡨࡹࠡࡴࡨࡴࡱࡧࡣࡪࡰࡪࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࡙࡮ࡥࠡࡥࡵࡩࡦࡺࡥࡥࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࡷࠥࡧࡲࡦࠢࡤࡨࡩ࡫ࡤࠡࡶࡲࠤࡹ࡮ࡥࠡࡪࡲࡳࡰ࠭ࡳࠡࠤ࡯ࡳ࡬ࡹࠢࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭࠽ࠤ࡙࡮ࡥࠡࡧࡹࡩࡳࡺࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴ࡭ࡳࠡࡣࡱࡨࠥ࡮࡯ࡰ࡭ࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᗥ")
        global _1l1llll1lll_opy_
        platform_index = os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᗦ")]
        bstack1ll111l1111_opy_ = os.path.join(bstack1ll11lll11l_opy_, (bstack1ll1111llll_opy_ + str(platform_index)), bstack11llll111ll_opy_)
        if not os.path.exists(bstack1ll111l1111_opy_) or not os.path.isdir(bstack1ll111l1111_opy_):
            self.logger.debug(bstack1l1_opy_ (u"ࠢࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷࡷࠥࡺ࡯ࠡࡲࡵࡳࡨ࡫ࡳࡴࠢࡾࢁࠧᗧ").format(bstack1ll111l1111_opy_))
            return
        logs = hook.get(bstack1l1_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᗨ"), [])
        with os.scandir(bstack1ll111l1111_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1l1llll1lll_opy_:
                    self.logger.info(bstack1l1_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢᗩ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1l1_opy_ (u"ࠥࠦᗪ")
                    log_entry = bstack1ll111ll111_opy_(
                        kind=bstack1l1_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᗫ"),
                        message=bstack1l1_opy_ (u"ࠧࠨᗬ"),
                        level=bstack1l1_opy_ (u"ࠨࠢᗭ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll1l1lll11_opy_=entry.stat().st_size,
                        bstack1ll1l11111l_opy_=bstack1l1_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢᗮ"),
                        bstack11l111l_opy_=os.path.abspath(entry.path),
                        bstack1ll1111lll1_opy_=hook.get(TestFramework.bstack1ll1l111l11_opy_)
                    )
                    logs.append(log_entry)
                    _1l1llll1lll_opy_.add(abs_path)
        platform_index = os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᗯ")]
        bstack1ll1l1l1111_opy_ = os.path.join(bstack1ll11lll11l_opy_, (bstack1ll1111llll_opy_ + str(platform_index)), bstack11llll111ll_opy_, bstack11llll11ll1_opy_)
        if not os.path.exists(bstack1ll1l1l1111_opy_) or not os.path.isdir(bstack1ll1l1l1111_opy_):
            self.logger.info(bstack1l1_opy_ (u"ࠤࡑࡳࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡬࡯ࡶࡰࡧࠤࡦࡺ࠺ࠡࡽࢀࠦᗰ").format(bstack1ll1l1l1111_opy_))
        else:
            self.logger.info(bstack1l1_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠿ࠦࡻࡾࠤᗱ").format(bstack1ll1l1l1111_opy_))
            with os.scandir(bstack1ll1l1l1111_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1l1llll1lll_opy_:
                        self.logger.info(bstack1l1_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤᗲ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1l1_opy_ (u"ࠧࠨᗳ")
                        log_entry = bstack1ll111ll111_opy_(
                            kind=bstack1l1_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᗴ"),
                            message=bstack1l1_opy_ (u"ࠢࠣᗵ"),
                            level=bstack1l1_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᗶ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll1l1lll11_opy_=entry.stat().st_size,
                            bstack1ll1l11111l_opy_=bstack1l1_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᗷ"),
                            bstack11l111l_opy_=os.path.abspath(entry.path),
                            bstack1ll11l1111l_opy_=hook.get(TestFramework.bstack1ll1l111l11_opy_)
                        )
                        logs.append(log_entry)
                        _1l1llll1lll_opy_.add(abs_path)
        hook[bstack1l1_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᗸ")] = logs
    def bstack1ll1111ll1l_opy_(
        self,
        bstack1ll111lllll_opy_: bstack1lll1l11111_opy_,
        entries: List[bstack1ll111ll111_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1l1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡘࡋࡓࡔࡋࡒࡒࡤࡏࡄࠣᗹ"))
        req.platform_index = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1lllll1l11l_opy_)
        req.execution_context.hash = str(bstack1ll111lllll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111lllll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111lllll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1lll1l1111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1lll1ll1l11_opy_)
            log_entry.uuid = entry.bstack1ll1111lll1_opy_
            log_entry.test_framework_state = bstack1ll111lllll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᗺ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack1l1_opy_ (u"ࠨࠢᗻ")
            if entry.kind == bstack1l1_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᗼ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l1lll11_opy_
                log_entry.file_path = entry.bstack11l111l_opy_
        def bstack1ll1l1l1l1l_opy_():
            bstack1l1ll111l_opy_ = datetime.now()
            try:
                self.bstack1llll1l11ll_opy_.LogCreatedEvent(req)
                bstack1ll111lllll_opy_.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᗽ"), datetime.now() - bstack1l1ll111l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࢁࡽࠣᗾ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1ll1_opy_.enqueue(bstack1ll1l1l1l1l_opy_)
    def __1ll11ll11ll_opy_(self, instance) -> None:
        bstack1l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡍࡱࡤࡨࡸࠦࡣࡶࡵࡷࡳࡲࠦࡴࡢࡩࡶࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡶࡪࡧࡴࡦࡵࠣࡥࠥࡪࡩࡤࡶࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡲࡥࡷࡧ࡯ࠤࡨࡻࡳࡵࡱࡰࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࡥࠢࡩࡶࡴࡳࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡸࡷࡹࡵ࡭ࡕࡣࡪࡑࡦࡴࡡࡨࡧࡵࠤࡦࡴࡤࠡࡷࡳࡨࡦࡺࡥࡴࠢࡷ࡬ࡪࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡵࡷࡥࡹ࡫ࠠࡶࡵ࡬ࡲ࡬ࠦࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᗿ")
        bstack1ll111l111l_opy_ = {bstack1l1_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࠨᘀ"): bstack1ll11llllll_opy_.bstack1l1llll1l11_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll1l11llll_opy_(instance, bstack1ll111l111l_opy_)
    @staticmethod
    def bstack1ll111lll11_opy_(instance: bstack1lll1l11111_opy_, bstack1ll11ll111l_opy_: str):
        bstack1ll1l1ll1l1_opy_ = (
            bstack1l11ll11lll_opy_.bstack1ll1l111l1l_opy_
            if bstack1ll11ll111l_opy_ == bstack1l11ll11lll_opy_.bstack1ll1l1l1ll1_opy_
            else bstack1l11ll11lll_opy_.bstack1ll11l111ll_opy_
        )
        bstack1ll1111l11l_opy_ = TestFramework.get_state(instance, bstack1ll11ll111l_opy_, None)
        bstack1ll1111111l_opy_ = TestFramework.get_state(instance, bstack1ll1l1ll1l1_opy_, None) if bstack1ll1111l11l_opy_ else None
        return (
            bstack1ll1111111l_opy_[bstack1ll1111l11l_opy_][-1]
            if isinstance(bstack1ll1111111l_opy_, dict) and len(bstack1ll1111111l_opy_.get(bstack1ll1111l11l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1l111lll_opy_(instance: bstack1lll1l11111_opy_, bstack1ll11ll111l_opy_: str):
        hook = bstack1l11ll11lll_opy_.bstack1ll111lll11_opy_(instance, bstack1ll11ll111l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1111l1ll_opy_, []).clear()
    @staticmethod
    def __1ll1l111111_opy_(instance: bstack1lll1l11111_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥᘁ"), None)):
            return
        if os.getenv(bstack1l1_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥᘂ"), bstack1l1_opy_ (u"ࠢ࠲ࠤᘃ")) != bstack1l1_opy_ (u"ࠣ࠳ࠥᘄ"):
            bstack1l11ll11lll_opy_.logger.warning(bstack1l1_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦᘅ"))
            return
        bstack1ll111l1ll1_opy_ = {
            bstack1l1_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᘆ"): (bstack1l11ll11lll_opy_.bstack1ll1l111ll1_opy_, bstack1l11ll11lll_opy_.bstack1ll11l111ll_opy_),
            bstack1l1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᘇ"): (bstack1l11ll11lll_opy_.bstack1ll1l1l1ll1_opy_, bstack1l11ll11lll_opy_.bstack1ll1l111l1l_opy_),
        }
        for when in (bstack1l1_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᘈ"), bstack1l1_opy_ (u"ࠨࡣࡢ࡮࡯ࠦᘉ"), bstack1l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᘊ")):
            bstack1ll11l11111_opy_ = args[1].get_records(when)
            if not bstack1ll11l11111_opy_:
                continue
            records = [
                bstack1ll111ll111_opy_(
                    kind=TestFramework.bstack1ll11111111_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦᘋ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥᘌ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11l11111_opy_
                if isinstance(getattr(r, bstack1l1_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᘍ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11l1llll_opy_, bstack1ll1l1ll1l1_opy_ = bstack1ll111l1ll1_opy_.get(when, (None, None))
            bstack1ll11111lll_opy_ = TestFramework.get_state(instance, bstack1ll11l1llll_opy_, None) if bstack1ll11l1llll_opy_ else None
            bstack1ll1111111l_opy_ = TestFramework.get_state(instance, bstack1ll1l1ll1l1_opy_, None) if bstack1ll11111lll_opy_ else None
            if isinstance(bstack1ll1111111l_opy_, dict) and len(bstack1ll1111111l_opy_.get(bstack1ll11111lll_opy_, [])) > 0:
                hook = bstack1ll1111111l_opy_[bstack1ll11111lll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1111l1ll_opy_ in hook:
                    hook[TestFramework.bstack1ll1111l1ll_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1l1lll1llll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11llll1l_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l11ll11lll_opy_.__1ll1l11l11l_opy_(test.location) if hasattr(test, bstack1l1_opy_ (u"ࠦࡱࡵࡣࡢࡶ࡬ࡳࡳࠨᘎ")) else getattr(test, bstack1l1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᘏ"), None)
        test_name = test.name if hasattr(test, bstack1l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᘐ")) else None
        bstack1l1llll11ll_opy_ = test.fspath.strpath if hasattr(test, bstack1l1_opy_ (u"ࠢࡧࡵࡳࡥࡹ࡮ࠢᘑ")) and test.fspath else None
        if not test_id or not test_name or not bstack1l1llll11ll_opy_:
            return None
        code = None
        if hasattr(test, bstack1l1_opy_ (u"ࠣࡱࡥ࡮ࠧᘒ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll111l1_opy_ = []
        try:
            bstack11llll111l1_opy_ = bstack1l111ll1_opy_.bstack1ll11l11_opy_(test)
        except:
            bstack1l11ll11lll_opy_.logger.warning(bstack1l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡸࡪࡹࡴࠡࡵࡦࡳࡵ࡫ࡳ࠭ࠢࡷࡩࡸࡺࠠࡴࡥࡲࡴࡪࡹࠠࡸ࡫࡯ࡰࠥࡨࡥࠡࡴࡨࡷࡴࡲࡶࡦࡦࠣ࡭ࡳࠦࡃࡍࡋࠥᘓ"))
        return {
            TestFramework.bstack1llll111ll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l1111l1_opy_: test_id,
            TestFramework.bstack1ll111ll1ll_opy_: test_name,
            TestFramework.bstack1ll1l11ll11_opy_: getattr(test, bstack1l1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᘔ"), None),
            TestFramework.bstack1l1llll1l1l_opy_: bstack1l1llll11ll_opy_,
            TestFramework.bstack1ll11lll1l1_opy_: bstack1l11ll11lll_opy_.__1ll11ll11l1_opy_(test),
            TestFramework.bstack1l1llll1ll1_opy_: code,
            TestFramework.bstack1lll1ll11ll_opy_: TestFramework.bstack1ll11l1ll11_opy_,
            TestFramework.bstack1lll1111l1l_opy_: test_id,
            TestFramework.bstack1l11111ll11_opy_: bstack11llll111l1_opy_
        }
    @staticmethod
    def __1ll11ll11l1_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack1l1_opy_ (u"ࠦࡴࡽ࡮ࡠ࡯ࡤࡶࡰ࡫ࡲࡴࠤᘕ"), [])
            markers.extend([getattr(m, bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᘖ"), None) for m in own_markers if getattr(m, bstack1l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᘗ"), None)])
            current = getattr(current, bstack1l1_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢᘘ"), None)
        return markers
    @staticmethod
    def __1ll1l11l11l_opy_(location):
        return bstack1l1_opy_ (u"ࠣ࠼࠽ࠦᘙ").join(filter(lambda x: isinstance(x, str), location))