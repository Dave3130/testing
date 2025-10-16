# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack11111111ll_opy_,
    bstack1lllllll1ll_opy_,
    bstack1lll11ll111_opy_,
    bstack1llllll11ll_opy_,
    bstack1lll1l11l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack111111111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_, bstack1llll1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lllll1_opy_ import bstack1llll111ll1_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1lll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11llll1_opy_(bstack1llll111ll1_opy_):
    bstack1lll1l1l1ll_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡴ࡬ࡺࡪࡸࡳࠣᅟ")
    bstack1llll11llll_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᅠ")
    bstack1lll1llll11_opy_ = bstack1ll1ll1_opy_ (u"ࠦࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᅡ")
    bstack1lll1l1llll_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅢ")
    bstack1llll1l111l_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡤࡸࡥࡧࡵࠥᅣ")
    bstack1llll11l111_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡩࡲࡦࡣࡷࡩࡩࠨᅤ")
    bstack1llll11lll1_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᅥ")
    bstack1lll1lll11l_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠢᅦ")
    def __init__(self):
        super().__init__(bstack1lll1l111l1_opy_=self.bstack1lll1l1l1ll_opy_, frameworks=[bstack111111111l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.BEFORE_EACH, bstack1llll1l11l1_opy_.POST), self.bstack1lll111ll1l_opy_)
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.TEST, bstack1llll1l11l1_opy_.PRE), self.bstack1llll111l11_opy_)
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll11l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll111ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11lll1l_opy_ = self.bstack1lll111lll1_opy_(instance.context)
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᅧ") + str(bstack1llll1l1lll_opy_) + bstack1ll1ll1_opy_ (u"ࠦࠧᅨ"))
        f.bstack1lllll1l1ll_opy_(instance, bstack1lll11llll1_opy_.bstack1llll11llll_opy_, bstack1lll11lll1l_opy_)
        bstack1lll11l11l1_opy_ = self.bstack1lll111lll1_opy_(instance.context, bstack1lll111ll11_opy_=False)
        f.bstack1lllll1l1ll_opy_(instance, bstack1lll11llll1_opy_.bstack1lll1llll11_opy_, bstack1lll11l11l1_opy_)
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111ll1l_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll11lll1_opy_, False):
            self.__1lll11lll11_opy_(f,instance,bstack1llll1l1lll_opy_)
    def bstack1llll11l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111ll1l_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll11lll1_opy_, False):
            self.__1lll11lll11_opy_(f, instance, bstack1llll1l1lll_opy_)
        if not f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1lll11l_opy_, False):
            self.__1lll11l1l1l_opy_(f, instance, bstack1llll1l1lll_opy_)
    def bstack1lll11l1ll1_opy_(
        self,
        f: bstack111111111l_opy_,
        driver: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11ll1l1_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1lll11l_opy_, False):
            return
        driver.execute_script(
            bstack1ll1ll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᅩ").format(
                json.dumps(
                    {
                        bstack1ll1ll1_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᅪ"): bstack1ll1ll1_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᅫ"),
                        bstack1ll1ll1_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᅬ"): {bstack1ll1ll1_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᅭ"): result},
                    }
                )
            )
        )
        f.bstack1lllll1l1ll_opy_(instance, bstack1lll11llll1_opy_.bstack1lll1lll11l_opy_, True)
    def bstack1lll111lll1_opy_(self, context: bstack1lll1l11l11_opy_, bstack1lll111ll11_opy_= True):
        if bstack1lll111ll11_opy_:
            bstack1lll11lll1l_opy_ = self.bstack1lll1l1l11l_opy_(context, reverse=True)
        else:
            bstack1lll11lll1l_opy_ = self.bstack1lll1ll11ll_opy_(context, reverse=True)
        return [f for f in bstack1lll11lll1l_opy_ if f[1].state != bstack11111111ll_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1l1lllll1l_opy_, stage=STAGE.bstack111l1l111_opy_)
    def __1lll11l1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll1ll1_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᅮ")).get(bstack1ll1ll1_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᅯ")):
            bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll11llll_opy_, [])
            if not bstack1lll11lll1l_opy_:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᅰ") + str(bstack1llll1l1lll_opy_) + bstack1ll1ll1_opy_ (u"ࠨࠢᅱ"))
                return
            driver = bstack1lll11lll1l_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_, None)
            if not status:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᅲ") + str(bstack1llll1l1lll_opy_) + bstack1ll1ll1_opy_ (u"ࠣࠤᅳ"))
                return
            bstack1llll111l1l_opy_ = {bstack1ll1ll1_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᅴ"): status.lower()}
            bstack1llll1111l1_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll1111_opy_, None)
            if status.lower() == bstack1ll1ll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᅵ") and bstack1llll1111l1_opy_ is not None:
                bstack1llll111l1l_opy_[bstack1ll1ll1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᅶ")] = bstack1llll1111l1_opy_[0][bstack1ll1ll1_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᅷ")][0] if isinstance(bstack1llll1111l1_opy_, list) else str(bstack1llll1111l1_opy_)
            driver.execute_script(
                bstack1ll1ll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᅸ").format(
                    json.dumps(
                        {
                            bstack1ll1ll1_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᅹ"): bstack1ll1ll1_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᅺ"),
                            bstack1ll1ll1_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅻ"): bstack1llll111l1l_opy_,
                        }
                    )
                )
            )
            f.bstack1lllll1l1ll_opy_(instance, bstack1lll11llll1_opy_.bstack1lll1lll11l_opy_, True)
    @measure(event_name=EVENTS.bstack11llllll11_opy_, stage=STAGE.bstack111l1l111_opy_)
    def __1lll11lll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll1ll1_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᅼ")).get(bstack1ll1ll1_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᅽ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll11l1lll_opy_, None)
            if not test_name:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᅾ"))
                return
            bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll11llll_opy_, [])
            if not bstack1lll11lll1l_opy_:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᅿ") + str(bstack1llll1l1lll_opy_) + bstack1ll1ll1_opy_ (u"ࠢࠣᆀ"))
                return
            for bstack1lll111llll_opy_, bstack1lll11ll11l_opy_ in bstack1lll11lll1l_opy_:
                if not bstack111111111l_opy_.bstack1lll11ll1l1_opy_(bstack1lll11ll11l_opy_):
                    continue
                driver = bstack1lll111llll_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1ll1ll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆁ").format(
                        json.dumps(
                            {
                                bstack1ll1ll1_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆂ"): bstack1ll1ll1_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᆃ"),
                                bstack1ll1ll1_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆄ"): {bstack1ll1ll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᆅ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1lllll1l1ll_opy_(instance, bstack1lll11llll1_opy_.bstack1llll11lll1_opy_, True)
    def bstack1lll1ll1l1l_opy_(
        self,
        instance: bstack1llll1l1111_opy_,
        f: TestFramework,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111ll1l_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        bstack1lll11lll1l_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll11llll_opy_, [])]
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᆆ"))
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᆇ"))
            return
        for bstack1lll11ll1ll_opy_ in bstack1lll11lll1l_opy_:
            driver = bstack1lll11ll1ll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1ll1ll1_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨᆈ") + str(timestamp)
            driver.execute_script(
                bstack1ll1ll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᆉ").format(
                    json.dumps(
                        {
                            bstack1ll1ll1_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᆊ"): bstack1ll1ll1_opy_ (u"ࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨᆋ"),
                            bstack1ll1ll1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᆌ"): {
                                bstack1ll1ll1_opy_ (u"ࠨࡴࡺࡲࡨࠦᆍ"): bstack1ll1ll1_opy_ (u"ࠢࡂࡰࡱࡳࡹࡧࡴࡪࡱࡱࠦᆎ"),
                                bstack1ll1ll1_opy_ (u"ࠣࡦࡤࡸࡦࠨᆏ"): data,
                                bstack1ll1ll1_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬ࠣᆐ"): bstack1ll1ll1_opy_ (u"ࠥࡨࡪࡨࡵࡨࠤᆑ")
                            }
                        }
                    )
                )
            )
    def bstack1llll1l1l11_opy_(
        self,
        instance: bstack1llll1l1111_opy_,
        f: TestFramework,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111ll1l_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        keys = [
            bstack1lll11llll1_opy_.bstack1llll11llll_opy_,
            bstack1lll11llll1_opy_.bstack1lll1llll11_opy_,
        ]
        bstack1lll11lll1l_opy_ = []
        for key in keys:
            bstack1lll11lll1l_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡡ࡯ࡻࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᆒ"))
            return
        if f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll11l111_opy_, False):
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡃࡃࡖࠣࡥࡱࡸࡥࡢࡦࡼࠤࡨࡸࡥࡢࡶࡨࡨࠧᆓ"))
            return
        self.bstack1llllll111l_opy_()
        bstack111lllll1_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1111111ll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll11111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll111111_opy_)
        req.test_framework_state = bstack1llll1l1lll_opy_[0].name
        req.test_hook_state = bstack1llll1l1lll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1l1l1l1_opy_)
        for bstack1lll111llll_opy_, driver in bstack1lll11lll1l_opy_:
            try:
                webdriver = bstack1lll111llll_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡗࡦࡤࡇࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠥ࠮ࡲࡦࡨࡨࡶࡪࡴࡣࡦࠢࡨࡼࡵ࡯ࡲࡦࡦࠬࠦᆔ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1ll1ll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨᆕ")
                    if bstack111111111l_opy_.get_state(driver, bstack111111111l_opy_.bstack1lll11l111l_opy_, False)
                    else bstack1ll1ll1_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠢᆖ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack111111111l_opy_.get_state(driver, bstack111111111l_opy_.bstack1llll11ll1l_opy_, bstack1ll1ll1_opy_ (u"ࠤࠥᆗ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack111111111l_opy_.get_state(driver, bstack111111111l_opy_.bstack1lll1l11l1l_opy_, bstack1ll1ll1_opy_ (u"ࠥࠦᆘ"))
                caps = None
                if hasattr(webdriver, bstack1ll1ll1_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᆙ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1ll1ll1_opy_ (u"࡙ࠧࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡤࡪࡴࡨࡧࡹࡲࡹࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷ࠴ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᆚ"))
                    except Exception as e:
                        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡪࡩࡹࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠱ࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠼ࠣࠦᆛ") + str(e) + bstack1ll1ll1_opy_ (u"ࠢࠣᆜ"))
                try:
                    bstack1lll11l11ll_opy_ = json.dumps(caps).encode(bstack1ll1ll1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᆝ")) if caps else bstack1lll11l1l11_opy_ (u"ࠤࡾࢁࠧᆞ")
                    req.capabilities = bstack1lll11l11ll_opy_
                except Exception as e:
                    self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡤࡤࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡱࡨࠥࡹࡥࡳ࡫ࡤࡰ࡮ࢀࡥࠡࡥࡤࡴࡸࠦࡦࡰࡴࠣࡶࡪࡷࡵࡦࡵࡷ࠾ࠥࠨᆟ") + str(e) + bstack1ll1ll1_opy_ (u"ࠦࠧᆠ"))
            except Exception as e:
                self.logger.error(bstack1ll1ll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡷࡩࡲࡀࠠࠣᆡ") + str(str(e)) + bstack1ll1ll1_opy_ (u"ࠨࠢᆢ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l1ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll11llll_opy_, [])
        if not bstack1lll1ll1lll_opy_() and len(bstack1lll11lll1l_opy_) == 0:
            bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1llll11_opy_, [])
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆣ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠣࠤᆤ"))
            return {}
        if len(bstack1lll11lll1l_opy_) > 1:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆥ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠥࠦᆦ"))
            return {}
        bstack1lll111llll_opy_, bstack1lll1ll11l1_opy_ = bstack1lll11lll1l_opy_[0]
        driver = bstack1lll111llll_opy_()
        if not driver:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆧ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠧࠨᆨ"))
            return {}
        capabilities = f.get_state(bstack1lll1ll11l1_opy_, bstack111111111l_opy_.bstack1llll111lll_opy_)
        if not capabilities:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆩ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠢࠣᆪ"))
            return {}
        return capabilities.get(bstack1ll1ll1_opy_ (u"ࠣࡣ࡯ࡻࡦࡿࡳࡎࡣࡷࡧ࡭ࠨᆫ"), {})
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll11llll_opy_, [])
        if not bstack1lll1ll1lll_opy_() and len(bstack1lll11lll1l_opy_) == 0:
            bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1lll1llll11_opy_, [])
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆬ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠥࠦᆭ"))
            return
        if len(bstack1lll11lll1l_opy_) > 1:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᆮ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠧࠨᆯ"))
        bstack1lll111llll_opy_, bstack1lll1ll11l1_opy_ = bstack1lll11lll1l_opy_[0]
        driver = bstack1lll111llll_opy_()
        if not driver:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆰ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠢࠣᆱ"))
            return
        return driver