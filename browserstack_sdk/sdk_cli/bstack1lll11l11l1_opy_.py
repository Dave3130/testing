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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import (
    bstack1llll1lll11_opy_,
    bstack1llll1ll111_opy_,
    bstack1lll111ll11_opy_,
    bstack1llllllll1l_opy_,
    bstack1lll1l111l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_, bstack1lll1llll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1111l_opy_ import bstack1llll11111l_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1llll1111ll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll111l11l_opy_(bstack1llll11111l_opy_):
    bstack1lll1ll11l1_opy_ = bstack1l1lll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡵ࡭ࡻ࡫ࡲࡴࠤᅙ")
    bstack1lll1llllll_opy_ = bstack1l1lll1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᅚ")
    bstack1lll1l1ll11_opy_ = bstack1l1lll1_opy_ (u"ࠧࡴ࡯࡯ࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᅛ")
    bstack1llll11l1l1_opy_ = bstack1l1lll1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᅜ")
    bstack1llll11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡥࡲࡦࡨࡶࠦᅝ")
    bstack1lll11lllll_opy_ = bstack1l1lll1_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡣࡳࡧࡤࡸࡪࡪࠢᅞ")
    bstack1lll1ll1l1l_opy_ = bstack1l1lll1_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟࡯ࡣࡰࡩࠧᅟ")
    bstack1llll111111_opy_ = bstack1l1lll1_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡵࡷࡥࡹࡻࡳࠣᅠ")
    def __init__(self):
        super().__init__(bstack1llll11l11l_opy_=self.bstack1lll1ll11l1_opy_, frameworks=[bstack1lllll111l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.BEFORE_EACH, bstack1lll1lll11l_opy_.POST), self.bstack1lll11l1lll_opy_)
        TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1lll1l111ll_opy_)
        TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1llll111l1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11l1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11l111l_opy_ = self.bstack1lll11l11ll_opy_(instance.context)
        if not bstack1lll11l111l_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᅡ") + str(bstack1lllll1llll_opy_) + bstack1l1lll1_opy_ (u"ࠧࠨᅢ"))
        f.bstack1llll1lllll_opy_(instance, bstack1lll111l11l_opy_.bstack1lll1llllll_opy_, bstack1lll11l111l_opy_)
        bstack1lll11ll1ll_opy_ = self.bstack1lll11l11ll_opy_(instance.context, bstack1lll111l1ll_opy_=False)
        f.bstack1llll1lllll_opy_(instance, bstack1lll111l11l_opy_.bstack1lll1l1ll11_opy_, bstack1lll11ll1ll_opy_)
    def bstack1lll1l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1ll1l1l_opy_, False):
            self.__1lll11l1l11_opy_(f,instance,bstack1lllll1llll_opy_)
    def bstack1llll111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1ll1l1l_opy_, False):
            self.__1lll11l1l11_opy_(f, instance, bstack1lllll1llll_opy_)
        if not f.get_state(instance, bstack1lll111l11l_opy_.bstack1llll111111_opy_, False):
            self.__1lll111l1l1_opy_(f, instance, bstack1lllll1llll_opy_)
    def bstack1lll11l1ll1_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll111llll_opy_(instance):
            return
        if f.get_state(instance, bstack1lll111l11l_opy_.bstack1llll111111_opy_, False):
            return
        driver.execute_script(
            bstack1l1lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᅣ").format(
                json.dumps(
                    {
                        bstack1l1lll1_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᅤ"): bstack1l1lll1_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᅥ"),
                        bstack1l1lll1_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅦ"): {bstack1l1lll1_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᅧ"): result},
                    }
                )
            )
        )
        f.bstack1llll1lllll_opy_(instance, bstack1lll111l11l_opy_.bstack1llll111111_opy_, True)
    def bstack1lll11l11ll_opy_(self, context: bstack1lll1l111l1_opy_, bstack1lll111l1ll_opy_= True):
        if bstack1lll111l1ll_opy_:
            bstack1lll11l111l_opy_ = self.bstack1llll111ll1_opy_(context, reverse=True)
        else:
            bstack1lll11l111l_opy_ = self.bstack1llll11ll1l_opy_(context, reverse=True)
        return [f for f in bstack1lll11l111l_opy_ if f[1].state != bstack1llll1lll11_opy_.QUIT]
    @measure(event_name=EVENTS.bstack111llll1l_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1lll111l1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᅨ")).get(bstack1l1lll1_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᅩ")):
            bstack1lll11l111l_opy_ = f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1llllll_opy_, [])
            if not bstack1lll11l111l_opy_:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᅪ") + str(bstack1lllll1llll_opy_) + bstack1l1lll1_opy_ (u"ࠢࠣᅫ"))
                return
            driver = bstack1lll11l111l_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1l11111_opy_, None)
            if not status:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᅬ") + str(bstack1lllll1llll_opy_) + bstack1l1lll1_opy_ (u"ࠤࠥᅭ"))
                return
            bstack1lll1l11l11_opy_ = {bstack1l1lll1_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᅮ"): status.lower()}
            bstack1lll1l1llll_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll111l_opy_, None)
            if status.lower() == bstack1l1lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᅯ") and bstack1lll1l1llll_opy_ is not None:
                bstack1lll1l11l11_opy_[bstack1l1lll1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᅰ")] = bstack1lll1l1llll_opy_[0][bstack1l1lll1_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᅱ")][0] if isinstance(bstack1lll1l1llll_opy_, list) else str(bstack1lll1l1llll_opy_)
            driver.execute_script(
                bstack1l1lll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᅲ").format(
                    json.dumps(
                        {
                            bstack1l1lll1_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᅳ"): bstack1l1lll1_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧᅴ"),
                            bstack1l1lll1_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᅵ"): bstack1lll1l11l11_opy_,
                        }
                    )
                )
            )
            f.bstack1llll1lllll_opy_(instance, bstack1lll111l11l_opy_.bstack1llll111111_opy_, True)
    @measure(event_name=EVENTS.bstack1l1ll1ll11_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1lll11l1l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᅶ")).get(bstack1l1lll1_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᅷ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll111lll1_opy_, None)
            if not test_name:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧᅸ"))
                return
            bstack1lll11l111l_opy_ = f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1llllll_opy_, [])
            if not bstack1lll11l111l_opy_:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᅹ") + str(bstack1lllll1llll_opy_) + bstack1l1lll1_opy_ (u"ࠣࠤᅺ"))
                return
            for bstack1lll11ll111_opy_, bstack1lll11ll1l1_opy_ in bstack1lll11l111l_opy_:
                if not bstack1lllll111l1_opy_.bstack1lll111llll_opy_(bstack1lll11ll1l1_opy_):
                    continue
                driver = bstack1lll11ll111_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1l1lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᅻ").format(
                        json.dumps(
                            {
                                bstack1l1lll1_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᅼ"): bstack1l1lll1_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᅽ"),
                                bstack1l1lll1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᅾ"): {bstack1l1lll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᅿ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llll1lllll_opy_(instance, bstack1lll111l11l_opy_.bstack1lll1ll1l1l_opy_, True)
    def bstack1llll11l1ll_opy_(
        self,
        instance: bstack1lll1llll11_opy_,
        f: TestFramework,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        bstack1lll11l111l_opy_ = [d for d, _ in f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1llllll_opy_, [])]
        if not bstack1lll11l111l_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡴࡰࠢ࡯࡭ࡳࡱࠢᆀ"))
            return
        if not bstack1llll1111ll_opy_():
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᆁ"))
            return
        for bstack1lll11l1l1l_opy_ in bstack1lll11l111l_opy_:
            driver = bstack1lll11l1l1l_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1l1lll1_opy_ (u"ࠤࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡕࡼࡲࡨࡀࠢᆂ") + str(timestamp)
            driver.execute_script(
                bstack1l1lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣᆃ").format(
                    json.dumps(
                        {
                            bstack1l1lll1_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᆄ"): bstack1l1lll1_opy_ (u"ࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢᆅ"),
                            bstack1l1lll1_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᆆ"): {
                                bstack1l1lll1_opy_ (u"ࠢࡵࡻࡳࡩࠧᆇ"): bstack1l1lll1_opy_ (u"ࠣࡃࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠧᆈ"),
                                bstack1l1lll1_opy_ (u"ࠤࡧࡥࡹࡧࠢᆉ"): data,
                                bstack1l1lll1_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࠤᆊ"): bstack1l1lll1_opy_ (u"ࠦࡩ࡫ࡢࡶࡩࠥᆋ")
                            }
                        }
                    )
                )
            )
    def bstack1llll1l1111_opy_(
        self,
        instance: bstack1lll1llll11_opy_,
        f: TestFramework,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        keys = [
            bstack1lll111l11l_opy_.bstack1lll1llllll_opy_,
            bstack1lll111l11l_opy_.bstack1lll1l1ll11_opy_,
        ]
        bstack1lll11l111l_opy_ = []
        for key in keys:
            bstack1lll11l111l_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11l111l_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡢࡰࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡴࡰࠢ࡯࡭ࡳࡱࠢᆌ"))
            return
        if f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll11lllll_opy_, False):
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡄࡄࡗࠤࡦࡲࡲࡦࡣࡧࡽࠥࡩࡲࡦࡣࡷࡩࡩࠨᆍ"))
            return
        self.bstack1llll1llll1_opy_()
        bstack11ll11ll1_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l1ll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll1l111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1l111_opy_)
        req.test_framework_state = bstack1lllll1llll_opy_[0].name
        req.test_hook_state = bstack1lllll1llll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11lll1_opy_)
        for bstack1lll11ll111_opy_, driver in bstack1lll11l111l_opy_:
            try:
                webdriver = bstack1lll11ll111_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡘࡧࡥࡈࡷ࡯ࡶࡦࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥ࡯ࡳࠡࡐࡲࡲࡪࠦࠨࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࠣࡩࡽࡶࡩࡳࡧࡧ࠭ࠧᆎ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1l1lll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢᆏ")
                    if bstack1lllll111l1_opy_.get_state(driver, bstack1lllll111l1_opy_.bstack1lll11ll11l_opy_, False)
                    else bstack1l1lll1_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠣᆐ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll111l1_opy_.get_state(driver, bstack1lllll111l1_opy_.bstack1lll1ll1ll1_opy_, bstack1l1lll1_opy_ (u"ࠥࠦᆑ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll111l1_opy_.get_state(driver, bstack1lllll111l1_opy_.bstack1llll11llll_opy_, bstack1l1lll1_opy_ (u"ࠦࠧᆒ"))
                caps = None
                if hasattr(webdriver, bstack1l1lll1_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᆓ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࡤࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡥ࡫ࡵࡩࡨࡺ࡬ࡺࠢࡩࡶࡴࡳࠠࡥࡴ࡬ࡺࡪࡸ࠮ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᆔ"))
                    except Exception as e:
                        self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡫ࡪࡺࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠲ࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠤࠧᆕ") + str(e) + bstack1l1lll1_opy_ (u"ࠣࠤᆖ"))
                try:
                    bstack1lll11l1111_opy_ = json.dumps(caps).encode(bstack1l1lll1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᆗ")) if caps else bstack1lll111ll1l_opy_ (u"ࠥࡿࢂࠨᆘ")
                    req.capabilities = bstack1lll11l1111_opy_
                except Exception as e:
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠦ࡬࡫ࡴࡠࡥࡥࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡲࡩࠦࡳࡦࡴ࡬ࡥࡱ࡯ࡺࡦࠢࡦࡥࡵࡹࠠࡧࡱࡵࠤࡷ࡫ࡱࡶࡧࡶࡸ࠿ࠦࠢᆙ") + str(e) + bstack1l1lll1_opy_ (u"ࠧࠨᆚ"))
            except Exception as e:
                self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡸࡪࡳ࠺ࠡࠤᆛ") + str(str(e)) + bstack1l1lll1_opy_ (u"ࠢࠣᆜ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1llll1111l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l111l_opy_ = f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1llllll_opy_, [])
        if not bstack1llll1111ll_opy_() and len(bstack1lll11l111l_opy_) == 0:
            bstack1lll11l111l_opy_ = f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1l1ll11_opy_, [])
        if not bstack1lll11l111l_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆝ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠤࠥᆞ"))
            return {}
        if len(bstack1lll11l111l_opy_) > 1:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆟ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠦࠧᆠ"))
            return {}
        bstack1lll11ll111_opy_, bstack1lll1ll1lll_opy_ = bstack1lll11l111l_opy_[0]
        driver = bstack1lll11ll111_opy_()
        if not driver:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᆡ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠨࠢᆢ"))
            return {}
        capabilities = f.get_state(bstack1lll1ll1lll_opy_, bstack1lllll111l1_opy_.bstack1lll1ll1111_opy_)
        if not capabilities:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᆣ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠣࠤᆤ"))
            return {}
        return capabilities.get(bstack1l1lll1_opy_ (u"ࠤࡤࡰࡼࡧࡹࡴࡏࡤࡸࡨ࡮ࠢᆥ"), {})
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l111l_opy_ = f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1llllll_opy_, [])
        if not bstack1llll1111ll_opy_() and len(bstack1lll11l111l_opy_) == 0:
            bstack1lll11l111l_opy_ = f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1l1ll11_opy_, [])
        if not bstack1lll11l111l_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆦ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠦࠧᆧ"))
            return
        if len(bstack1lll11l111l_opy_) > 1:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆨ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠨࠢᆩ"))
        bstack1lll11ll111_opy_, bstack1lll1ll1lll_opy_ = bstack1lll11l111l_opy_[0]
        driver = bstack1lll11ll111_opy_()
        if not driver:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆪ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠣࠤᆫ"))
            return
        return driver