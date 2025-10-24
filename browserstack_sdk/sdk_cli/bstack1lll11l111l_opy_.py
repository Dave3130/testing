# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack11111111ll_opy_ import (
    bstack1lllllll11l_opy_,
    bstack1llll1l11l1_opy_,
    bstack1lll111llll_opy_,
    bstack1lllll111ll_opy_,
    bstack1llll111l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_, bstack1lll1l11111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1llllll_opy_ import bstack1lll11lll1l_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l1111l_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll111lll1_opy_(bstack1lll11lll1l_opy_):
    bstack1lll1l11l1l_opy_ = bstack11l11l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢᅳ")
    bstack1llll11l1l1_opy_ = bstack11l11l1_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᅴ")
    bstack1lll1l111l1_opy_ = bstack11l11l1_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅵ")
    bstack1lll11ll11l_opy_ = bstack11l11l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᅶ")
    bstack1lll11ll1l1_opy_ = bstack11l11l1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤᅷ")
    bstack1llll111ll1_opy_ = bstack11l11l1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧᅸ")
    bstack1llll11l11l_opy_ = bstack11l11l1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᅹ")
    bstack1lll1lll1l1_opy_ = bstack11l11l1_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨᅺ")
    def __init__(self):
        super().__init__(bstack1lll1llll1l_opy_=self.bstack1lll1l11l1l_opy_, frameworks=[bstack1llll1lll1l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llll1l1l11_opy_((bstack1lll1l1lll1_opy_.BEFORE_EACH, bstack1lll1ll1111_opy_.POST), self.bstack1lll111l111_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1lll1l1lll1_opy_.TEST, bstack1lll1ll1111_opy_.PRE), self.bstack1lll1ll11l1_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1lll1l1lll1_opy_.TEST, bstack1lll1ll1111_opy_.POST), self.bstack1lll1ll1lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll111l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11111ll_opy_ = self.bstack1lll11l1111_opy_(instance.context)
        if not bstack1lll11111ll_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᅻ") + str(bstack1lllllll1l1_opy_) + bstack11l11l1_opy_ (u"ࠥࠦᅼ"))
        f.bstack1llllllllll_opy_(instance, bstack1lll111lll1_opy_.bstack1llll11l1l1_opy_, bstack1lll11111ll_opy_)
        bstack1lll111ll1l_opy_ = self.bstack1lll11l1111_opy_(instance.context, bstack1lll11l1l1l_opy_=False)
        f.bstack1llllllllll_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1l111l1_opy_, bstack1lll111ll1l_opy_)
    def bstack1lll1ll11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l111_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l11l_opy_, False):
            self.__1lll1111l11_opy_(f,instance,bstack1lllllll1l1_opy_)
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l111_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l11l_opy_, False):
            self.__1lll1111l11_opy_(f, instance, bstack1lllllll1l1_opy_)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1lll1l1_opy_, False):
            self.__1lll111l1l1_opy_(f, instance, bstack1lllllll1l1_opy_)
    def bstack1lll11l1l11_opy_(
        self,
        f: bstack1llll1lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll1111ll1_opy_(instance):
            return
        if f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1lll1l1_opy_, False):
            return
        driver.execute_script(
            bstack11l11l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᅽ").format(
                json.dumps(
                    {
                        bstack11l11l1_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᅾ"): bstack11l11l1_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᅿ"),
                        bstack11l11l1_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᆀ"): {bstack11l11l1_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᆁ"): result},
                    }
                )
            )
        )
        f.bstack1llllllllll_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1lll1l1_opy_, True)
    def bstack1lll11l1111_opy_(self, context: bstack1llll111l1l_opy_, bstack1lll11l1l1l_opy_= True):
        if bstack1lll11l1l1l_opy_:
            bstack1lll11111ll_opy_ = self.bstack1lll1l1ll1l_opy_(context, reverse=True)
        else:
            bstack1lll11111ll_opy_ = self.bstack1lll1ll111l_opy_(context, reverse=True)
        return [f for f in bstack1lll11111ll_opy_ if f[1].state != bstack1lllllll11l_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1l1l111l11_opy_, stage=STAGE.bstack1ll1lllll_opy_)
    def __1lll111l1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l11l1_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᆂ")).get(bstack11l11l1_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᆃ")):
            bstack1lll11111ll_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l1l1_opy_, [])
            if not bstack1lll11111ll_opy_:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᆄ") + str(bstack1lllllll1l1_opy_) + bstack11l11l1_opy_ (u"ࠧࠨᆅ"))
                return
            driver = bstack1lll11111ll_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll11lll11_opy_, None)
            if not status:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᆆ") + str(bstack1lllllll1l1_opy_) + bstack11l11l1_opy_ (u"ࠢࠣᆇ"))
                return
            bstack1llll111l11_opy_ = {bstack11l11l1_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᆈ"): status.lower()}
            bstack1llll1111ll_opy_ = f.get_state(instance, TestFramework.bstack1lll1l11lll_opy_, None)
            if status.lower() == bstack11l11l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᆉ") and bstack1llll1111ll_opy_ is not None:
                bstack1llll111l11_opy_[bstack11l11l1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᆊ")] = bstack1llll1111ll_opy_[0][bstack11l11l1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᆋ")][0] if isinstance(bstack1llll1111ll_opy_, list) else str(bstack1llll1111ll_opy_)
            driver.execute_script(
                bstack11l11l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᆌ").format(
                    json.dumps(
                        {
                            bstack11l11l1_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᆍ"): bstack11l11l1_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᆎ"),
                            bstack11l11l1_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᆏ"): bstack1llll111l11_opy_,
                        }
                    )
                )
            )
            f.bstack1llllllllll_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1lll1l1_opy_, True)
    @measure(event_name=EVENTS.bstack1ll11111ll_opy_, stage=STAGE.bstack1ll1lllll_opy_)
    def __1lll1111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l11l1_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᆐ")).get(bstack11l11l1_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᆑ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll1111l1l_opy_, None)
            if not test_name:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᆒ"))
                return
            bstack1lll11111ll_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l1l1_opy_, [])
            if not bstack1lll11111ll_opy_:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᆓ") + str(bstack1lllllll1l1_opy_) + bstack11l11l1_opy_ (u"ࠨࠢᆔ"))
                return
            for bstack1lll11l11l1_opy_, bstack1lll111ll11_opy_ in bstack1lll11111ll_opy_:
                if not bstack1llll1lll1l_opy_.bstack1lll1111ll1_opy_(bstack1lll111ll11_opy_):
                    continue
                driver = bstack1lll11l11l1_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11l11l1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᆕ").format(
                        json.dumps(
                            {
                                bstack11l11l1_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᆖ"): bstack11l11l1_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥᆗ"),
                                bstack11l11l1_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆘ"): {bstack11l11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᆙ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llllllllll_opy_(instance, bstack1lll111lll1_opy_.bstack1llll11l11l_opy_, True)
    def bstack1llll11111l_opy_(
        self,
        instance: bstack1lll1l11111_opy_,
        f: TestFramework,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l111_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        bstack1lll11111ll_opy_ = [d for d, _ in f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l1l1_opy_, [])]
        if not bstack1lll11111ll_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤࡹࡵࠠ࡭࡫ࡱ࡯ࠧᆚ"))
            return
        if not bstack1lll1l1111l_opy_():
            self.logger.debug(bstack11l11l1_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᆛ"))
            return
        for bstack1lll1111lll_opy_ in bstack1lll11111ll_opy_:
            driver = bstack1lll1111lll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11l11l1_opy_ (u"ࠢࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡓࡺࡰࡦ࠾ࠧᆜ") + str(timestamp)
            driver.execute_script(
                bstack11l11l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆝ").format(
                    json.dumps(
                        {
                            bstack11l11l1_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆞ"): bstack11l11l1_opy_ (u"ࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧᆟ"),
                            bstack11l11l1_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆠ"): {
                                bstack11l11l1_opy_ (u"ࠧࡺࡹࡱࡧࠥᆡ"): bstack11l11l1_opy_ (u"ࠨࡁ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠥᆢ"),
                                bstack11l11l1_opy_ (u"ࠢࡥࡣࡷࡥࠧᆣ"): data,
                                bstack11l11l1_opy_ (u"ࠣ࡮ࡨࡺࡪࡲࠢᆤ"): bstack11l11l1_opy_ (u"ࠤࡧࡩࡧࡻࡧࠣᆥ")
                            }
                        }
                    )
                )
            )
    def bstack1llll11l111_opy_(
        self,
        instance: bstack1lll1l11111_opy_,
        f: TestFramework,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l111_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        keys = [
            bstack1lll111lll1_opy_.bstack1llll11l1l1_opy_,
            bstack1lll111lll1_opy_.bstack1lll1l111l1_opy_,
        ]
        bstack1lll11111ll_opy_ = []
        for key in keys:
            bstack1lll11111ll_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11111ll_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧ࡮ࡺࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤࡹࡵࠠ࡭࡫ࡱ࡯ࠧᆦ"))
            return
        if f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll111ll1_opy_, False):
            self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡉࡂࡕࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡧࡷ࡫ࡡࡵࡧࡧࠦᆧ"))
            return
        self.bstack1llll1lllll_opy_()
        bstack1l11lll1ll_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll11111_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1ll11_opy_)
        req.test_framework_state = bstack1lllllll1l1_opy_[0].name
        req.test_hook_state = bstack1lllllll1l1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        for bstack1lll11l11l1_opy_, driver in bstack1lll11111ll_opy_:
            try:
                webdriver = bstack1lll11l11l1_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11l11l1_opy_ (u"ࠧ࡝ࡥࡣࡆࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠤ࠭ࡸࡥࡧࡧࡵࡩࡳࡩࡥࠡࡧࡻࡴ࡮ࡸࡥࡥࠫࠥᆨ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11l11l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧᆩ")
                    if bstack1llll1lll1l_opy_.get_state(driver, bstack1llll1lll1l_opy_.bstack1lll11l11ll_opy_, False)
                    else bstack11l11l1_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨᆪ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1llll1lll1l_opy_.get_state(driver, bstack1llll1lll1l_opy_.bstack1lll1l1l1l1_opy_, bstack11l11l1_opy_ (u"ࠣࠤᆫ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1llll1lll1l_opy_.get_state(driver, bstack1llll1lll1l_opy_.bstack1lll1l1l11l_opy_, bstack11l11l1_opy_ (u"ࠤࠥᆬ"))
                caps = None
                if hasattr(webdriver, bstack11l11l1_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᆭ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡶࡪࡺࡲࡪࡧࡹࡩࡩࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥࡪࡩࡳࡧࡦࡸࡱࡿࠠࡧࡴࡲࡱࠥࡪࡲࡪࡸࡨࡶ࠳ࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᆮ"))
                    except Exception as e:
                        self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡩࡨࡸࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠰ࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠻ࠢࠥᆯ") + str(e) + bstack11l11l1_opy_ (u"ࠨࠢᆰ"))
                try:
                    bstack1lll111l11l_opy_ = json.dumps(caps).encode(bstack11l11l1_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᆱ")) if caps else bstack1lll111l1ll_opy_ (u"ࠣࡽࢀࠦᆲ")
                    req.capabilities = bstack1lll111l11l_opy_
                except Exception as e:
                    self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡪࡩࡹࡥࡣࡣࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡰࡧࠤࡸ࡫ࡲࡪࡣ࡯࡭ࡿ࡫ࠠࡤࡣࡳࡷࠥ࡬࡯ࡳࠢࡵࡩࡶࡻࡥࡴࡶ࠽ࠤࠧᆳ") + str(e) + bstack11l11l1_opy_ (u"ࠥࠦᆴ"))
            except Exception as e:
                self.logger.error(bstack11l11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡥࡴ࡬ࡺࡪࡸࠠࡪࡶࡨࡱ࠿ࠦࠢᆵ") + str(str(e)) + bstack11l11l1_opy_ (u"ࠧࠨᆶ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l1l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11111ll_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l1l1_opy_, [])
        if not bstack1lll1l1111l_opy_() and len(bstack1lll11111ll_opy_) == 0:
            bstack1lll11111ll_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l111l1_opy_, [])
        if not bstack1lll11111ll_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆷ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠢࠣᆸ"))
            return {}
        if len(bstack1lll11111ll_opy_) > 1:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆹ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠤࠥᆺ"))
            return {}
        bstack1lll11l11l1_opy_, bstack1lll11ll1ll_opy_ = bstack1lll11111ll_opy_[0]
        driver = bstack1lll11l11l1_opy_()
        if not driver:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆻ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠦࠧᆼ"))
            return {}
        capabilities = f.get_state(bstack1lll11ll1ll_opy_, bstack1llll1lll1l_opy_.bstack1lll1lll11l_opy_)
        if not capabilities:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆽ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠨࠢᆾ"))
            return {}
        return capabilities.get(bstack11l11l1_opy_ (u"ࠢࡢ࡮ࡺࡥࡾࡹࡍࡢࡶࡦ࡬ࠧᆿ"), {})
    def bstack1lll1ll1l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11111ll_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l1l1_opy_, [])
        if not bstack1lll1l1111l_opy_() and len(bstack1lll11111ll_opy_) == 0:
            bstack1lll11111ll_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l111l1_opy_, [])
        if not bstack1lll11111ll_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇀ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠤࠥᇁ"))
            return
        if len(bstack1lll11111ll_opy_) > 1:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇂ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠦࠧᇃ"))
        bstack1lll11l11l1_opy_, bstack1lll11ll1ll_opy_ = bstack1lll11111ll_opy_[0]
        driver = bstack1lll11l11l1_opy_()
        if not driver:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇄ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠨࠢᇅ"))
            return
        return driver