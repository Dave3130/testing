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
import os
from uuid import uuid4
from bstack_utils.helper import bstack1ll1llll_opy_, bstack111l11l1lll_opy_
from bstack_utils.bstack111l111ll_opy_ import bstack11l11l11l11_opy_
class bstack1ll1l1l1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack11111l11111_opy_=None, bstack111111lll1l_opy_=True, bstack1l1lllll1ll_opy_=None, bstack11l111ll1_opy_=None, result=None, duration=None, bstack1l1l11l1_opy_=None, meta={}):
        self.bstack1l1l11l1_opy_ = bstack1l1l11l1_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111lll1l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack11111l11111_opy_ = bstack11111l11111_opy_
        self.bstack1l1lllll1ll_opy_ = bstack1l1lllll1ll_opy_
        self.bstack11l111ll1_opy_ = bstack11l111ll1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1lll1ll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11ll1lll_opy_(self, meta):
        self.meta = meta
    def bstack11l1l1l1_opy_(self, hooks):
        self.hooks = hooks
    def bstack11111l1111l_opy_(self):
        bstack11111l1l111_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1l1lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩụ"): bstack11111l1l111_opy_,
            bstack1l1lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩỦ"): bstack11111l1l111_opy_,
            bstack1l1lll1_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭ủ"): bstack11111l1l111_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1l1lll1_opy_ (u"ࠤࡘࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡸࡱࡪࡴࡴ࠻ࠢࠥỨ") + key)
            setattr(self, key, val)
    def bstack111111lll11_opy_(self):
        return {
            bstack1l1lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨứ"): self.name,
            bstack1l1lll1_opy_ (u"ࠫࡧࡵࡤࡺࠩỪ"): {
                bstack1l1lll1_opy_ (u"ࠬࡲࡡ࡯ࡩࠪừ"): bstack1l1lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭Ử"),
                bstack1l1lll1_opy_ (u"ࠧࡤࡱࡧࡩࠬử"): self.code
            },
            bstack1l1lll1_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨỮ"): self.scope,
            bstack1l1lll1_opy_ (u"ࠩࡷࡥ࡬ࡹࠧữ"): self.tags,
            bstack1l1lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭Ự"): self.framework,
            bstack1l1lll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨự"): self.started_at
        }
    def bstack111111lllll_opy_(self):
        return {
         bstack1l1lll1_opy_ (u"ࠬࡳࡥࡵࡣࠪỲ"): self.meta
        }
    def bstack11111l11l11_opy_(self):
        return {
            bstack1l1lll1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡘࡥࡳࡷࡱࡔࡦࡸࡡ࡮ࠩỳ"): {
                bstack1l1lll1_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠫỴ"): self.bstack11111l11111_opy_
            }
        }
    def bstack11111l111l1_opy_(self, bstack11111l11ll1_opy_, details):
        step = next(filter(lambda st: st[bstack1l1lll1_opy_ (u"ࠨ࡫ࡧࠫỵ")] == bstack11111l11ll1_opy_, self.meta[bstack1l1lll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨỶ")]), None)
        step.update(details)
    def bstack11ll111l_opy_(self, bstack11111l11ll1_opy_):
        step = next(filter(lambda st: st[bstack1l1lll1_opy_ (u"ࠪ࡭ࡩ࠭ỷ")] == bstack11111l11ll1_opy_, self.meta[bstack1l1lll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪỸ")]), None)
        step.update({
            bstack1l1lll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩỹ"): bstack1ll1llll_opy_()
        })
    def bstack1l1l1ll1_opy_(self, bstack11111l11ll1_opy_, result, duration=None):
        bstack1l1lllll1ll_opy_ = bstack1ll1llll_opy_()
        if bstack11111l11ll1_opy_ is not None and self.meta.get(bstack1l1lll1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬỺ")):
            step = next(filter(lambda st: st[bstack1l1lll1_opy_ (u"ࠧࡪࡦࠪỻ")] == bstack11111l11ll1_opy_, self.meta[bstack1l1lll1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧỼ")]), None)
            step.update({
                bstack1l1lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧỽ"): bstack1l1lllll1ll_opy_,
                bstack1l1lll1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬỾ"): duration if duration else bstack111l11l1lll_opy_(step[bstack1l1lll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨỿ")], bstack1l1lllll1ll_opy_),
                bstack1l1lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬἀ"): result.result,
                bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧἁ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111ll11l_opy_):
        if self.meta.get(bstack1l1lll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ἂ")):
            self.meta[bstack1l1lll1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧἃ")].append(bstack111111ll11l_opy_)
        else:
            self.meta[bstack1l1lll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἄ")] = [ bstack111111ll11l_opy_ ]
    def bstack111111ll1l1_opy_(self):
        return {
            bstack1l1lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨἅ"): self.bstack1lll1ll1_opy_(),
            **self.bstack111111lll11_opy_(),
            **self.bstack11111l1111l_opy_(),
            **self.bstack111111lllll_opy_()
        }
    def bstack11111l11lll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1l1lll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩἆ"): self.bstack1l1lllll1ll_opy_,
            bstack1l1lll1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ἇ"): self.duration,
            bstack1l1lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭Ἀ"): self.result.result
        }
        if data[bstack1l1lll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧἉ")] == bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨἊ"):
            data[bstack1l1lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨἋ")] = self.result.bstack11111l1111_opy_()
            data[bstack1l1lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫἌ")] = [{bstack1l1lll1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧἍ"): self.result.bstack111l1lll111_opy_()}]
        return data
    def bstack11111l111ll_opy_(self):
        return {
            bstack1l1lll1_opy_ (u"ࠬࡻࡵࡪࡦࠪἎ"): self.bstack1lll1ll1_opy_(),
            **self.bstack111111lll11_opy_(),
            **self.bstack11111l1111l_opy_(),
            **self.bstack11111l11lll_opy_(),
            **self.bstack111111lllll_opy_()
        }
    def bstack1l1lll11_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1l1lll1_opy_ (u"࠭ࡓࡵࡣࡵࡸࡪࡪࠧἏ") in event:
            return self.bstack111111ll1l1_opy_()
        elif bstack1l1lll1_opy_ (u"ࠧࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩἐ") in event:
            return self.bstack11111l111ll_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1l1lllll1ll_opy_ = time if time else bstack1ll1llll_opy_()
        self.duration = duration if duration else bstack111l11l1lll_opy_(self.started_at, self.bstack1l1lllll1ll_opy_)
        if result:
            self.result = result
class bstack1l1111ll_opy_(bstack1ll1l1l1_opy_):
    def __init__(self, hooks=[], bstack1ll11l11_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1ll11l11_opy_ = bstack1ll11l11_opy_
        super().__init__(*args, **kwargs, bstack11l111ll1_opy_=bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ἑ"))
    @classmethod
    def bstack11111l11l1l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1lll1_opy_ (u"ࠩ࡬ࡨࠬἒ"): id(step),
                bstack1l1lll1_opy_ (u"ࠪࡸࡪࡾࡴࠨἓ"): step.name,
                bstack1l1lll1_opy_ (u"ࠫࡰ࡫ࡹࡸࡱࡵࡨࠬἔ"): step.keyword,
            })
        return bstack1l1111ll_opy_(
            **kwargs,
            meta={
                bstack1l1lll1_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪ࠭ἕ"): {
                    bstack1l1lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ἖"): feature.name,
                    bstack1l1lll1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ἗"): feature.filename,
                    bstack1l1lll1_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭Ἐ"): feature.description
                },
                bstack1l1lll1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫἙ"): {
                    bstack1l1lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨἚ"): scenario.name
                },
                bstack1l1lll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἛ"): steps,
                bstack1l1lll1_opy_ (u"ࠬ࡫ࡸࡢ࡯ࡳࡰࡪࡹࠧἜ"): bstack11l11l11l11_opy_(test)
            }
        )
    def bstack111111llll1_opy_(self):
        return {
            bstack1l1lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬἝ"): self.hooks
        }
    def bstack111111ll1ll_opy_(self):
        if self.bstack1ll11l11_opy_:
            return {
                bstack1l1lll1_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭἞"): self.bstack1ll11l11_opy_
            }
        return {}
    def bstack11111l111ll_opy_(self):
        return {
            **super().bstack11111l111ll_opy_(),
            **self.bstack111111llll1_opy_()
        }
    def bstack111111ll1l1_opy_(self):
        return {
            **super().bstack111111ll1l1_opy_(),
            **self.bstack111111ll1ll_opy_()
        }
    def event_key(self):
        return bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ἟")
class bstack1l111lll_opy_(bstack1ll1l1l1_opy_):
    def __init__(self, hook_type, *args,bstack1ll11l11_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111lll1l_opy_ = None
        self.bstack1ll11l11_opy_ = bstack1ll11l11_opy_
        super().__init__(*args, **kwargs, bstack11l111ll1_opy_=bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧἠ"))
    def bstack1l11llll_opy_(self):
        return self.hook_type
    def bstack111111ll111_opy_(self):
        return {
            bstack1l1lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ἡ"): self.hook_type
        }
    def bstack11111l111ll_opy_(self):
        return {
            **super().bstack11111l111ll_opy_(),
            **self.bstack111111ll111_opy_()
        }
    def bstack111111ll1l1_opy_(self):
        return {
            **super().bstack111111ll1l1_opy_(),
            bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡩࡥࠩἢ"): self.bstack1l1111lll1l_opy_,
            **self.bstack111111ll111_opy_()
        }
    def event_key(self):
        return bstack1l1lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧἣ")
    def bstack11ll1l1l_opy_(self, bstack1l1111lll1l_opy_):
        self.bstack1l1111lll1l_opy_ = bstack1l1111lll1l_opy_