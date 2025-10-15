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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import (
    bstack1lllll11l1l_opy_,
    bstack1111111lll_opy_,
    bstack1lll11l1111_opy_,
    bstack1llllllll1l_opy_,
    bstack1lll1l1ll1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll11l11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_, bstack1lll1l1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1lll_opy_ import bstack1lll1ll1l11_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1llll1l_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11l1ll1_opy_(bstack1lll1ll1l11_opy_):
    bstack1llll11lll1_opy_ = bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡴ࡬ࡺࡪࡸࡳࠣᅘ")
    bstack1llll1l11l1_opy_ = bstack1ll1l_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᅙ")
    bstack1lll1ll111l_opy_ = bstack1ll1l_opy_ (u"ࠦࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᅚ")
    bstack1lll1l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅛ")
    bstack1lll1l1l1l1_opy_ = bstack1ll1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡤࡸࡥࡧࡵࠥᅜ")
    bstack1llll11ll11_opy_ = bstack1ll1l_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡩࡲࡦࡣࡷࡩࡩࠨᅝ")
    bstack1lll1lll111_opy_ = bstack1ll1l_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᅞ")
    bstack1llll111l11_opy_ = bstack1ll1l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠢᅟ")
    def __init__(self):
        super().__init__(bstack1lll1ll1ll1_opy_=self.bstack1llll11lll1_opy_, frameworks=[bstack1lllll11l11_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.BEFORE_EACH, bstack1lll1llll11_opy_.POST), self.bstack1lll11l1lll_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.TEST, bstack1lll1llll11_opy_.PRE), self.bstack1llll11111l_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.TEST, bstack1lll1llll11_opy_.POST), self.bstack1llll11l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll11l1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11l11l1_opy_ = self.bstack1lll11ll1ll_opy_(instance.context)
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᅠ") + str(bstack1llllll111l_opy_) + bstack1ll1l_opy_ (u"ࠦࠧᅡ"))
        f.bstack1111111ll1_opy_(instance, bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_, bstack1lll11l11l1_opy_)
        bstack1lll11lll11_opy_ = self.bstack1lll11ll1ll_opy_(instance.context, bstack1lll11l1l1l_opy_=False)
        f.bstack1111111ll1_opy_(instance, bstack1lll11l1ll1_opy_.bstack1lll1ll111l_opy_, bstack1lll11lll11_opy_)
    def bstack1llll11111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1llllll111l_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1lll1lll111_opy_, False):
            self.__1lll11l111l_opy_(f,instance,bstack1llllll111l_opy_)
    def bstack1llll11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1llllll111l_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1lll1lll111_opy_, False):
            self.__1lll11l111l_opy_(f, instance, bstack1llllll111l_opy_)
        if not f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1llll111l11_opy_, False):
            self.__1lll11l11ll_opy_(f, instance, bstack1llllll111l_opy_)
    def bstack1lll11l1l11_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll111ll1l_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1llll111l11_opy_, False):
            return
        driver.execute_script(
            bstack1ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᅢ").format(
                json.dumps(
                    {
                        bstack1ll1l_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᅣ"): bstack1ll1l_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᅤ"),
                        bstack1ll1l_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᅥ"): {bstack1ll1l_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᅦ"): result},
                    }
                )
            )
        )
        f.bstack1111111ll1_opy_(instance, bstack1lll11l1ll1_opy_.bstack1llll111l11_opy_, True)
    def bstack1lll11ll1ll_opy_(self, context: bstack1lll1l1ll1l_opy_, bstack1lll11l1l1l_opy_= True):
        if bstack1lll11l1l1l_opy_:
            bstack1lll11l11l1_opy_ = self.bstack1lll1lll1l1_opy_(context, reverse=True)
        else:
            bstack1lll11l11l1_opy_ = self.bstack1lll1l111l1_opy_(context, reverse=True)
        return [f for f in bstack1lll11l11l1_opy_ if f[1].state != bstack1lllll11l1l_opy_.QUIT]
    @measure(event_name=EVENTS.bstack11llll1l1_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def __1lll11l11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᅧ")).get(bstack1ll1l_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᅨ")):
            bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_, [])
            if not bstack1lll11l11l1_opy_:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᅩ") + str(bstack1llllll111l_opy_) + bstack1ll1l_opy_ (u"ࠨࠢᅪ"))
                return
            driver = bstack1lll11l11l1_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1l11l1l_opy_, None)
            if not status:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᅫ") + str(bstack1llllll111l_opy_) + bstack1ll1l_opy_ (u"ࠣࠤᅬ"))
                return
            bstack1llll111ll1_opy_ = {bstack1ll1l_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᅭ"): status.lower()}
            bstack1llll1l1111_opy_ = f.get_state(instance, TestFramework.bstack1llll1111ll_opy_, None)
            if status.lower() == bstack1ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᅮ") and bstack1llll1l1111_opy_ is not None:
                bstack1llll111ll1_opy_[bstack1ll1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᅯ")] = bstack1llll1l1111_opy_[0][bstack1ll1l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᅰ")][0] if isinstance(bstack1llll1l1111_opy_, list) else str(bstack1llll1l1111_opy_)
            driver.execute_script(
                bstack1ll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᅱ").format(
                    json.dumps(
                        {
                            bstack1ll1l_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᅲ"): bstack1ll1l_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᅳ"),
                            bstack1ll1l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅴ"): bstack1llll111ll1_opy_,
                        }
                    )
                )
            )
            f.bstack1111111ll1_opy_(instance, bstack1lll11l1ll1_opy_.bstack1llll111l11_opy_, True)
    @measure(event_name=EVENTS.bstack11lllll11l_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def __1lll11l111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᅵ")).get(bstack1ll1l_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᅶ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll111llll_opy_, None)
            if not test_name:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᅷ"))
                return
            bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_, [])
            if not bstack1lll11l11l1_opy_:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᅸ") + str(bstack1llllll111l_opy_) + bstack1ll1l_opy_ (u"ࠢࠣᅹ"))
                return
            for bstack1lll11ll111_opy_, bstack1lll11lll1l_opy_ in bstack1lll11l11l1_opy_:
                if not bstack1lllll11l11_opy_.bstack1lll111ll1l_opy_(bstack1lll11lll1l_opy_):
                    continue
                driver = bstack1lll11ll111_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1ll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᅺ").format(
                        json.dumps(
                            {
                                bstack1ll1l_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᅻ"): bstack1ll1l_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᅼ"),
                                bstack1ll1l_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᅽ"): {bstack1ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᅾ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1111111ll1_opy_(instance, bstack1lll11l1ll1_opy_.bstack1lll1lll111_opy_, True)
    def bstack1lll1lll1ll_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        f: TestFramework,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1llllll111l_opy_, *args, **kwargs)
        bstack1lll11l11l1_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_, [])]
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᅿ"))
            return
        if not bstack1lll1llll1l_opy_():
            self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᆀ"))
            return
        for bstack1lll111lll1_opy_ in bstack1lll11l11l1_opy_:
            driver = bstack1lll111lll1_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1ll1l_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨᆁ") + str(timestamp)
            driver.execute_script(
                bstack1ll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᆂ").format(
                    json.dumps(
                        {
                            bstack1ll1l_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᆃ"): bstack1ll1l_opy_ (u"ࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨᆄ"),
                            bstack1ll1l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᆅ"): {
                                bstack1ll1l_opy_ (u"ࠨࡴࡺࡲࡨࠦᆆ"): bstack1ll1l_opy_ (u"ࠢࡂࡰࡱࡳࡹࡧࡴࡪࡱࡱࠦᆇ"),
                                bstack1ll1l_opy_ (u"ࠣࡦࡤࡸࡦࠨᆈ"): data,
                                bstack1ll1l_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬ࠣᆉ"): bstack1ll1l_opy_ (u"ࠥࡨࡪࡨࡵࡨࠤᆊ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1l1l111_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        f: TestFramework,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll11l1lll_opy_(f, instance, bstack1llllll111l_opy_, *args, **kwargs)
        keys = [
            bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_,
            bstack1lll11l1ll1_opy_.bstack1lll1ll111l_opy_,
        ]
        bstack1lll11l11l1_opy_ = []
        for key in keys:
            bstack1lll11l11l1_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡡ࡯ࡻࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᆋ"))
            return
        if f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1llll11ll11_opy_, False):
            self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡃࡃࡖࠣࡥࡱࡸࡥࡢࡦࡼࠤࡨࡸࡥࡢࡶࡨࡨࠧᆌ"))
            return
        self.bstack1lllll1l111_opy_()
        bstack1l11l11lll_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllllllll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll11llll_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        req.test_framework_state = bstack1llllll111l_opy_[0].name
        req.test_hook_state = bstack1llllll111l_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11ll1l_opy_)
        for bstack1lll11ll111_opy_, driver in bstack1lll11l11l1_opy_:
            try:
                webdriver = bstack1lll11ll111_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡗࡦࡤࡇࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠥ࠮ࡲࡦࡨࡨࡶࡪࡴࡣࡦࠢࡨࡼࡵ࡯ࡲࡦࡦࠬࠦᆍ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1ll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨᆎ")
                    if bstack1lllll11l11_opy_.get_state(driver, bstack1lllll11l11_opy_.bstack1lll11ll1l1_opy_, False)
                    else bstack1ll1l_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠢᆏ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll11l11_opy_.get_state(driver, bstack1lllll11l11_opy_.bstack1llll11l11l_opy_, bstack1ll1l_opy_ (u"ࠤࠥᆐ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll11l11_opy_.get_state(driver, bstack1lllll11l11_opy_.bstack1lll1l1llll_opy_, bstack1ll1l_opy_ (u"ࠥࠦᆑ"))
                caps = None
                if hasattr(webdriver, bstack1ll1l_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᆒ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1ll1l_opy_ (u"࡙ࠧࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡤࡪࡴࡨࡧࡹࡲࡹࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷ࠴ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᆓ"))
                    except Exception as e:
                        self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡪࡩࡹࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠱ࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠼ࠣࠦᆔ") + str(e) + bstack1ll1l_opy_ (u"ࠢࠣᆕ"))
                try:
                    bstack1lll11ll11l_opy_ = json.dumps(caps).encode(bstack1ll1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᆖ")) if caps else bstack1lll111ll11_opy_ (u"ࠤࡾࢁࠧᆗ")
                    req.capabilities = bstack1lll11ll11l_opy_
                except Exception as e:
                    self.logger.debug(bstack1ll1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡤࡤࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡱࡨࠥࡹࡥࡳ࡫ࡤࡰ࡮ࢀࡥࠡࡥࡤࡴࡸࠦࡦࡰࡴࠣࡶࡪࡷࡵࡦࡵࡷ࠾ࠥࠨᆘ") + str(e) + bstack1ll1l_opy_ (u"ࠦࠧᆙ"))
            except Exception as e:
                self.logger.error(bstack1ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡷࡩࡲࡀࠠࠣᆚ") + str(str(e)) + bstack1ll1l_opy_ (u"ࠨࠢᆛ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1lllll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_, [])
        if not bstack1lll1llll1l_opy_() and len(bstack1lll11l11l1_opy_) == 0:
            bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1lll1ll111l_opy_, [])
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆜ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠣࠤᆝ"))
            return {}
        if len(bstack1lll11l11l1_opy_) > 1:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆞ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠥࠦᆟ"))
            return {}
        bstack1lll11ll111_opy_, bstack1lll1ll1l1l_opy_ = bstack1lll11l11l1_opy_[0]
        driver = bstack1lll11ll111_opy_()
        if not driver:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆠ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠧࠨᆡ"))
            return {}
        capabilities = f.get_state(bstack1lll1ll1l1l_opy_, bstack1lllll11l11_opy_.bstack1lll1l1111l_opy_)
        if not capabilities:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆢ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠢࠣᆣ"))
            return {}
        return capabilities.get(bstack1ll1l_opy_ (u"ࠣࡣ࡯ࡻࡦࡿࡳࡎࡣࡷࡧ࡭ࠨᆤ"), {})
    def bstack1lll1llllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_, [])
        if not bstack1lll1llll1l_opy_() and len(bstack1lll11l11l1_opy_) == 0:
            bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1lll1ll111l_opy_, [])
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᆥ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠥࠦᆦ"))
            return
        if len(bstack1lll11l11l1_opy_) > 1:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᆧ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠧࠨᆨ"))
        bstack1lll11ll111_opy_, bstack1lll1ll1l1l_opy_ = bstack1lll11l11l1_opy_[0]
        driver = bstack1lll11ll111_opy_()
        if not driver:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆩ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠢࠣᆪ"))
            return
        return driver